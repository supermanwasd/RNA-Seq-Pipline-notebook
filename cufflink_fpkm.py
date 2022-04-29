SAMPLES = ["SRR7469489_wt_ligule_stage2_rep1_b73","SRR7469522_mu_ligule_stage2_rep1_b73" , "SRR7469538_wt_ligule_stage1_rep1_b73"
,"SRR7469491_wt_ligule_stage3_rep3_b73" , "SRR7469524_wt_ligule_stage3_rep2_b73" , "SRR7469539_mu_ligule_stage4_rep1_b73"
,"SRR7469492_wt_ligule_stage4_rep1_b73" , "SRR7469525_mu_ligule_stage1_rep3_b73" , "SRR7469540_wt_ligule_stage1_rep3_b73"
,"SRR7469501_mu_ligule_stage4_rep2_b73" , "SRR7469526_wt_ligule_stage4_rep2_b73" , "SRR7469541_wt_ligule_stage2_rep3_b73"
,"SRR7469502_mu_ligule_stage4_rep3_b73" , "SRR7469527_mu_ligule_stage3_rep3_b73" , "SRR7469543_mu_ligule_stage2_rep3_b73"
,"SRR7469506_mu_ligule_stage0_rep1_b73" , "SRR7469530_wt_ligule_stage0_rep1_b73" , "SRR7469544_mu_ligule_stage2_rep2_b73"
,"SRR7469514_wt_ligule_stage0_rep3_b73" , "SRR7469531_wt_ligule_stage2_rep2_b73" , "SRR7469545_mu_ligule_stage3_rep2_b73"
,"SRR7469515_mu_ligule_stage0_rep2_b73" , "SRR7469533_wt_ligule_stage3_rep1_b73" , "SRR7469546_mu_ligule_stage3_rep1_b73"
,"SRR7469516_mu_ligule_stage0_rep3_b73" , "SRR7469536_wt_ligule_stage0_rep2_b73" , "SRR7469547_mu_ligule_stage1_rep2_b73"
,"SRR7469520_wt_ligule_stage4_rep3_b73" , "SRR7469537_wt_ligule_stage1_rep2_b73" , "SRR7469548_mu_ligule_stage1_rep1_b73"]

for smp in SAMPLES:
	print("Sample " + smp + " will be processed")

rule all:
	input:
		expand("assembly/{sample}",sample = SAMPLES)

rule bam_file_sort:
	input:
		"/media/14t/wyc/LIGULELESS1/L_lg2/sort/ligule/{sample}.bam"
	output:
		"/media/14t/wyc/LIGULELESS1/L_lg2/ligule/{sample}_sort.bam"
	shell:
		"samtools sort  -o {output} {input}"

rule assembly:
    input:
        "/media/14t/wyc/LIGULELESS1/L_lg2/ligule/{sample}_sort.bam"
    output:
        dir='assembly/{sample}'
    shell:
        'cufflinks -p 4 -G /media/8tb/Zea_may/plant_genome/Zea/Zmays_493_RefGen_V4.gene.gtf -o {output.dir} {input}'

        