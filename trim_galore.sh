#!/bin/bash
ls partly_raw_data | grep "_R1_001" > gz1
ls partly_raw_data | grep "_R2_001" > gz2
paste gz1 gz2>config_file
cat config_file
cat config_file | while read id
do
sample_dir="./partly_raw_data"
output_dir="./partly_raw_data_clean"
arr=($id)
fq1=${arr[0]}
fq2=${arr[1]}
sample_dir1="$sample_dir/$fq1"
sample_dir2="$sample_dir/$fq2"
trim_galore -q 25 --phred33 --length 36 -e 0.1 --stringency 3 --paired -o $output_dir $sample_dir1 $sample_dir2
done