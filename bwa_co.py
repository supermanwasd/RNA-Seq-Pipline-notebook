#2022.5.13
SAMPLES = ["S001_sdau-A_CIMBL125-ATAC-1_BH7KGWCCX2_S1_L008","S031_sdau-A_1313--2_BH7KGWCCX2_S31_L008"]

for smp in SAMPLES:
	print("Sample " + smp + " will be processed")

rule all:
	input:
		expand("/media/disk_first/wyc_data/atac_160/process_partly_raw_data/bam_data/{sample}_sort.bam",sample = SAMPLES)


rule fastp:
    input:
        R1 = "/media/disk_first/wyc_data/atac_160/partly_raw_data/{sample}_R1_001.fastq.gz",
        R2 = "/media/disk_first/wyc_data/atac_160/partly_raw_data/{sample}_R2_001.fastq.gz"
    output:
        O1 = "/media/disk_first/wyc_data/atac_160/process_partly_raw_data/fastp_data/{sample}_R1_fastp.fastq.gz",
        O2 = "/media/disk_first/wyc_data/atac_160/process_partly_raw_data/fastp_data/{sample}_R2_fastp.fastq.gz"
    shell:
        "fastp -i {input.R1} -I {input.R2} -o {output.O1} -O {output.O2}"

rule bwa:
	input:
		R1 = "/media/disk_first/wyc_data/atac_160/process_partly_raw_data/fastp_data/{sample}_R1_fastp.fastq.gz",
		R2 = "/media/disk_first/wyc_data/atac_160/process_partly_raw_data/fastp_data/{sample}_R2_fastp.fastq.gz"
	output:
		"/media/disk_first/wyc_data/atac_160/process_partly_raw_data/bam_data/{sample}.bam"
	shell:
		"bwa mem -M -t 10 -k 32 /media/8tb/Zea_may/all_index/bwa/Zeamay {input.R1} {input.R2}|samtools view -@ 8 -bh -q 30 -Sb - > {output}"

rule sort_bam:
	input:
		"/media/disk_first/wyc_data/atac_160/process_partly_raw_data/bam_data/{sample}.bam"
	output:
		"/media/disk_first/wyc_data/atac_160/process_partly_raw_data/bam_data/{sample}_sort.bam"
	shell:
		"samtools sort -@ 8 {input} -o {output}"
