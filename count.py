SAMPLES, = glob_wildcards("/media/amd/14t/wyc/LIGULELESS1/L_lg2/{sample}.fastq.gz")

for smp in SAMPLES:
    print("Sample " + smp + " will be processed")

rule all:
    input:
        expand("sort/{sample}_b73.bam",sample = SAMPLES),
        "counts/gene_counts.txt",
        "result/fpkm.csv"

rule mapping:
    input:
        R1 = "/media/amd/14t/wyc/LIGULELESS1/L_lg2/{sample}.fastq.gz"
    output:
        "map/{sample}.sam"
    log:
        "log/{sample}_B73.log"
    shell:
        "hisat2 -p 10 -x /media/8tb/Zea_may/v4/maize_v4 -U  {input.R1} -S {output} 1>{log} 2>&1"

rule bam_file_sort:
    input:
        "map/{sample}.sam"
    output:
        "sort/{sample}_b73.bam"
    shell:
        "samtools view -@ 8 -b -h -o {output} {input}"

rule quantification_with_featureCounts:
    input: 
        novel="/media/8tb/Zea_may/Zea_v4/Zea_mays.B73_RefGen_v4.45.gtf", bam=expand("sort/{sample}_b73.bam",sample = SAMPLES)
    output:
        "counts/gene_counts.txt"
    shell:"""
        featureCounts -T 60 -t exon -g gene_id -a {input.novel} -o {output} {input.bam}
        """
rule tpm_flow_DEG:
    input:
        counts = "counts/gene_counts.txt"
    output:
        tpm = "result/fpkm.csv"
    shell:"""
        Rscript cal_fpkm.r {input.counts} {output.tpm}
        """
