################################################################
#2020-11-16
#YunChuan Wang
#RNA-Seq Pipline
################################################################

SAMPLES = ['SRR4089365_PPDK_HL1_heter_1cm','SRR4089365_PPDK_HL1_heter_1cm',\
'SRR4089401_PPDK_LL1_homo_4cm','SRR4089366_PPDK_HL1_heter_4cm',\
'SRR4089404_PPDK_LL1_WT_1cm',\
'SRR4089369_PPDK_HL2_heter_1cm','SRR4089405_PPDK_LL1_WT_4cm',\
'SRR4089370_PPDK_HL2_heter_4cm','SRR4089408_PPDK_LL2_heter_1cm',\
'SRR4089373_PPDK_HL2_homo_1cm','SRR4089409_PPDK_LL2_heter_4cm',\
'SRR4089374_PPDK_HL2_homo_4cm','SRR4089410_PPDK_HL1_homo_4cm',\
'SRR4089378_PPDK_HL2_WT_1cm','SRR4089413_PPDK_LL2_homo_1cm',\
'SRR4089379_PPDK_HL2_WT_4cm','SRR4089414_PPDK_LL2_homo_4cm',\
'SRR4089382_PPDK_HL3_heter_1cm','SRR4089417_PPDK_LL2_WT_1cm',\
'SRR4089383_PPDK_HL3_heter_4cm','SRR4089418_PPDK_LL2_WT_4cm',\
'SRR4089386_PPDK_HL3_homo_1cm','SRR4089422_PPDK_LL3_heter_1cm',\
'SRR4089387_PPDK_HL3_homo_4cm','SRR4089423_PPDK_LL3_heter_4cm',\
'SRR4089391_PPDK_HL3_WT_1cm','SRR4089426_PPDK_LL3_homo_1cm',\
'SRR4089392_PPDK_HL3_WT_4cm','SRR4089427_PPDK_LL3_homo_4cm',\
'SRR4089395_PPDK_LL1_heter_1cm','SRR4089430_PPDK_LL3_WT_1cm',\
'SRR4089396_PPDK_LL1_heter_4cm','SRR4089431_PPDK_LL3_WT_4cm',\
'SRR4089399_PPDK_HL1_homo_1cm','SRR4089435_PPDK_HL1_WT_1cm',\
'SRR4089400_PPDK_LL1_homo_1cm','SRR4089436_PPDK_HL1_WT_4cm']


rule all:
	input:
		expand("map/{sample}.sam",sample = SAMPLES)

rule trim:
	input:
		"/media/amd/8tb/paper_Data/PPDK/{sample}.fastq"
	output:
		"cut/{sample}.fastq"
	shell:
		"java -jar /home/amd/Software/Trimmomatic-0.39/trimmomatic-0.39.jar SE -threads 60 \
		{input} {output} \
		ILLUMINACLIP:/home/amd/Software/Trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10 \
		LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30"

rule mapping:
	input:
		"cut/{sample}.fastq"
	output:
		"map/{sample}.sam"
	log:
		"log/{sample}-B73.log"
	shell:
		"hisat2 -p 60 -x /media/amd/8tb/Zea_may_hisat2_Data/Zm_B73_v4 -U {input} -S {output}  &> {log}"
