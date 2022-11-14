SAMPLES, = glob_wildcards("/X/{sample}_1.clean.fq.gz")

for smp in SAMPLES:
	print("Sample " + smp + " will be processed")

rule all:
	input:
		expand("sort/{sample}_b73v4.bam",sample = SAMPLES),
		expand("counts/gene_counts.txt")

rule mapping:
	input:
		R1 = "/X/{sample}_1.clean.fq.gz",
		R2 = "/X/{sample}_2.clean.fq.gz",
	output:
		"map/{sample}.sam"
	log:
		"log/{sample}_B73.log"
	threads: 20
	shell:
		"hisat2 -p {threads} --dta-cufflinks -x /media/8tb/Zea_may/v4/maize_v4  -1 {input.R1} -2 {input.R2}  -S {output} 1>{log} 2>&1"

rule bam_sam:
	input:
		"map/{sample}.sam"
	output:
		"sort/{sample}_b73v4.bam"
	threads: 20
	shell:
		"samtools view -@ {threads} -b -h -o {output} {input}"

rule quantification_with_featureCounts:
    input: 
    	novel="/media/8tb/Zea_may/Zea_v4/Zea_mays.B73_RefGen_v4.45.gtf", bam=expand("sort/{sample}_b73v4.bam",sample = SAMPLES)
    output:
    	"counts/gene_counts.txt"
    shell:"""
        featureCounts -T 60 -t exon -g gene_id -a {input.novel} -o {output} {input.bam}
        """
