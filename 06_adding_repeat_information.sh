# Loading in approproate modules
module load bedtools

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files 
bedtools intersect -wa -wb \
-a <PATH>/mean_low_coverage_genes \
-b selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,12,13,14 > <PATH>/genes_mean_repeat_annotation

# Removing duplicate lines following sorting
sort -k1,1 -k2,2 -k3,3 <PATH>/genes_mean_repeat_annotation | uniq > rmdup
mv rmdup <PATH>/genes_mean_repeat_annotation

### Pct coverage genes	intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/pct_low_coverage_genes \
-b selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,12,13,14 > <PATH>/genes_pct_repeat_annotation

# Removing duplicate lines following sorting
sort -k1,1 -k2,2 -k3,3 <PATH>/genes_pct_repeat_annotation | uniq > rmdup
mv rmdup <PATH>/genes_pct_repeat_annotation

### Mean coverage exons	intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/mean_low_coverage_exons \
-b selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,8,13,14,15 > <PATH>/exons_mean_repeat_annotaion

# Removing duplicate lines following sorting
sort -k1,1 -k2,2 -k3,3 <PATH>/exons_mean_repeat_annotation | uniq > rmdup
mv rmdup <PATH>/exons_mean_repeat_annotation

### Pct coverage exons intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/pct_low_coverage_exons \
-b selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,8,13,14,15 > <PATH>/exons_pct_repeat_annotation

# Removing duplicate lines following sorting
sort -k1,1 -k2,2 -k3,3 <PATH>/exons_pct_repeat_annotation | uniq > rmdup
mv rmdup <PATH>/exons_pct_repeat_annotation
