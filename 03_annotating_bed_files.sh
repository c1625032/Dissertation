# Loading in approproate module.
module load bedtools

### Gene annotation files

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf.
bedtools intersect -wa -wb \
# User can select any bed file as all have the same co-ordinates, this can be checked by cutting co-ordinate columns and checking for differences with uniq function.
-a <PATH_to_data>/<FILE>.bed \
-b <PATH_to_resources>/Homo_sapiens.GRCh37.75.gtf | \
# Filtering for genes.
awk -F "\t" '$10 == "gene"' | \
# Keeping selected columns.
cut -f 1,2,3,14,16 > <OUTPUT_DIRECTORY>/annotation/gene_bed_file.bed

# Moving into annotaion directory.
cd <OUTPUT_DIRECTORY>/annotation/

# Splitting gene_bed_file.bed so the final column containing information split by ; can can be seperated.
cut -f1,2,3,4 gene_bed_file.bed > first_half_gene_bed_file.bed
cut -f5 gene_bed_file.bed > second_half_gene_bed_file.bed

# Splitting gene information column.
awk 'BEGIN{OFS="\t" } { gsub(";","\t ",$0); print $0} ' second_half_gene_bed_file.bed > split_second_half_gene_bed_file.bed

# Pasting both halves back together, possible as indexes remain the same. 
paste -d "\t" first_half_gene_bed_file.bed split_second_half_gene_bed_file.bed > gene_bed_file.bed

# Removing unwanted common features within file.
sed -i 's/"//g' gene_bed_file.bed
sed -i 's/ //g' gene_bed_file.bed
sed -i 's/  //g' gene_bed_file.bed
sed -i 's/gene_id//g' gene_bed_file.bed
sed -i 's/gene_name//g' gene_bed_file.bed
sed -i 's/gene_source//g' gene_bed_file.bed
sed -i 's/gene_biotype//g' gene_bed_file.bed

# Filtering for protein coding genes.
awk -F "\t" '$8 == "protein_coding"' gene_bed_file.bed > protein_coding_only_gene_bed_file.bed 

# Keeping selected columns.
cut -f1,2,3,4,5,6 protein_coding_only_gene_bed_file.bed > gene_bed_file.bed

# Removing temp files.
rm protein_coding_only_gene_bed_file.bed first_half_gene_bed_file.bed split_second_half_gene_bed_file.bed second_half_gene_bed_file.bed

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 gene_bed_file.bed | uniq > rmdup
mv rmdup gene_bed_file.bed

### Exon annotation file.

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf.
bedtools intersect -wa -wb \
# User can select any bed file as all have the same co-ordinates, this can be checked by cutting co-ordinate columns and checking for differences with uniq function.
-a <PATH_to_data>/<FILE> \
-b <PATH_to_resources>/Homo_sapiens.GRCh37.75.gtf | \
# Filtering just for exons.
awk -F "\t" '$10 == "exon"' | \
# Keeping selected columns.
cut -f 1,2,3,14,16 > <OUTPUT_DIRECTORY>/annotation/exon_bed_file.bed

# Moving into annotation directory.
cd <OUTPUT_DIRECTORY>/annotation/

# Splitting exon_bed_file.bed so the final column containing information split by ; can can be seperated.
cut -f1,2,3,4 exon_bed_file.bed > first_half_exon_bed_file.bed
cut -f5 exon_bed_file.bed > second_half_exon_bed_file.bed

# Splitting gene information column.
awk 'BEGIN{OFS="\t" } { gsub(";","\t ",$0); print $0} ' second_half_exon_bed_file.bed > split_second_half_exon_bed_file.bed

# Pasting both halves back together, possible as indexes remain the same. 
paste -d "\t" first_half_exon_bed_file.bed split_second_half_exon_bed_file.bed > exon_bed_file.bed

# Removing unwanted common features.
sed -i 's/"//g' exon_bed_file.bed
sed -i 's/ //g' exon_bed_file.bed
sed -i 's/  //g' exon_bed_file.bed
sed -i 's/gene_id//g' exon_bed_file.bed
sed -i 's/transcript_id//g' exon_bed_file.bed
sed -i 's/exon_number//g' exon_bed_file.bed
sed -i 's/gene_name//g' exon_bed_file.bed
sed -i 's/gene_source//g' exon_bed_file.bed
sed -i 's/gene_biotype//g' exon_bed_file.bed
sed -i 's/transcript_name//g' exon_bed_file.bed
sed -i 's/transcript_source//g' exon_bed_file.bed
sed -i 's/exon_id//g' exon_bed_file.bed
sed -i 's/tag//g' exon_bed_file.bed

# Filtering for protein coding genes.
awk -F "\t" '$10 == "protein_coding"' exon_bed_file.bed > protein_coding_only_annotated_bed_file.bed

# Keeping selected columns.
cut -f1,2,3,4,5,7,8 protein_coding_only_annotated_bed_file.bed > exon_bed_file.bed

# Removing temp files.
rm protein_coding_only_annotated_bed_file.bed first_half_exon_bed_file.bed split_second_half_exon_bed_file.bed second_half_exon_bed_file.bed

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 exon_bed_file.bed | uniq > rmdup
mv rmdup exon_bed_file.bed
