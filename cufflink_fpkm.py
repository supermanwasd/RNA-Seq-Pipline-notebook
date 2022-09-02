SAMPLES, = glob_wildcards("sort/{sample}_b73v4.bam")

for smp in SAMPLES:
	print("Sample " + smp + " will be processed")

rule all:
	input:
		expand("assembly/{sample}",sample = SAMPLES)

rule bam_file_sort:
	input:
		"sort/{sample}_b73v4.bam"
	output:
		"sort/{sample}_sort.bam"
	threads: 10
	shell:
		"samtools sort -@ {threads} -o {output} {input}"

rule assembly:
    input:
        "sort/{sample}_sort.bam"
    output:
        directory('assembly/{sample}')
    threads: 10
    shell:
        'cufflinks -p {threads} -G /media/8tb/Zea_may/plant_genome/Zea/Zmays_493_RefGen_V4.gene.gtf -o {output} {input}'

        