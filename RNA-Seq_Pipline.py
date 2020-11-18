################################################################
#2020-11-16
#YunChuan Wang
#RNA-Seq Pipline
################################################################
REP_INDEX = {"SRR1573513_GSM1502515_wtL-1","SRR1573513_GSM1502515_wtL-1"}

rule all:
	input:
		expand("map/{rep}-B73-REFERENCE-GRAMENE-4.bam",rep = REP_INDEX),
		expand("fpkm/{rep}_B73.csv",rep = REP_INDEX),
		expand("count/{rep}_B73.txt",rep = REP_INDEX)


rule trim:
	input:
		"{rep}_Zea_mays_RNA-Seq_1.fastq",
		"{rep}_Zea_mays_RNA-Seq_2.fastq"
		
	output:
		"cut/{rep}_R1_paired.fastq",
		"cut/{rep}_R1_unpaired.fastq",
		"cut/{rep}_R2_paired.fastq",
		"cut/{rep}_R2_unpaired.fastq"
	shell:
		"java -jar /home/amd/Software/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 30 \
		{input[0]} {input[1]} {output[0]} {output[1]} {output[2]} {output[3]} \
		ILLUMINACLIP:/home/amd/Software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10 \
		LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30"

rule mapping:
	input:
		"cut/{rep}_R1_paired.fastq",
		"cut/{rep}_R2_paired.fastq"
	output:
		"map/{rep}.sam"
	shell:
		"gsnap -D /media/amd/8tb/Zea_may/Zea_v4/gmap_build/ -d maizev4 \
		--nthreads=30 -B 5 -N 1 -n 1 -Q \
		--nofails --format=sam \
		{input[0]} {input[1]}> {output[0]}"

rule bam_file_sort:
	input:
		"map/{rep}.sam"
	output:
		"map/{rep}-B73-REFERENCE-GRAMENE-4.bam"
	log:
		"map/{rep}-B73-REFERENCE-GRAMENE-4.log"
	shell:
		"samtools sort -O BAM -o {output} -T {log}.temp -@ 30 {input}"

rule cal_count:
	input:
		"map/{rep}-B73-REFERENCE-GRAMENE-4.bam"
	output:
		"count/{rep}_B73.txt"
	shell:
		"htseq-count -f bam {input} \
		/media/amd/8tb/Zea_may/Zea_v4/Zm-B73-REFERENCE-GRAMENE-4.0.gtf > {output}"

rule cal_fpkm:
	input:
		"map/{rep}-B73-REFERENCE-GRAMENE-4.bam"
	output:
		"fpkm/{rep}_B73"
	shell:
		"cufflinks -p 32 -G\
		/media/amd/8tb/Zea_may/Zea_v4/Zm-B73-REFERENCE-GRAMENE-4.0.gtf \
		 {input} -o {output}"