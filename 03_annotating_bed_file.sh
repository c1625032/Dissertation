# Loading in approproate modules
module load bedtools

# Calling bedtools intersect function and specifying it should provide all information from the original files 
bedtools intersect -wa -wb \
-a ../data/200518_A00748_0027_AHLKFCDRXX_19M15338.qc-coverage-region-1_cov_report.bed \
-b ../resources/Homo_sapiens.GRCh37.75.gtf | \
# Filtering just for genes
awk -F "\t" '$10 == "gene"' | \
# Keeping selected columns
cut -f 1,2,3,14,16 > ../output/annotated_bed_file.bed

# Moving into output directory
cd /scratch/c.c1625032/dissertation/output

# Splitting annotated_bed_file.bed so the final columns can be seperated
cut -f1,2,3,4 annotated_bed_file.bed > first_half_annotated_bed_file.bed
cut -f5 annotated_bed_file.bed > second_half_annotated_bed_file.bed

# Splitting gene information column
awk 'BEGIN{OFS="\t" } { gsub(";","\t ",$0); print $0} ' second_half_annotated_bed_file.bed > split_second_half_annotated_bed_file.bed

# Pasting both halves back together
paste -d "\t" first_half_annotated_bed_file.bed split_second_half_annotated_bed_file.bed > annotated_bed_file.bed

# Removing unwanted common features
sed -i 's/"//g' annotated_bed_file.bed
sed -i 's/ //g' annotated_bed_file.bed
sed -i 's/  //g' annotated_bed_file.bed
sed -i 's/gene_id//g' annotated_bed_file.bed
sed -i 's/gene_name//g' annotated_bed_file.bed
sed -i 's/gene_source//g' annotated_bed_file.bed
sed -i 's/gene_biotype//g' annotated_bed_file.bed

# Filtering for protein coding genes
awk -F "\t" '$8 == "protein_coding"' annotated_bed_file.bed > protein_coding_only_annotated_bed_file.bed 

# Keeping selected columns
cut -f1,2,3,4,5,6 protein_coding_only_annotated_bed_file.bed > annotated_bed_file.bed

# Removing temp files
rm protein_coding_only_annotated_bed_file.bed first_half_annotated_bed_file.bed split_second_half_annotated_bed_file.bed second_half_annotated_bed_file.bed

