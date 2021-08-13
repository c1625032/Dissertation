# Loading in approproate module.
module load bedtools

# Entering output directory
cd <PATH_to_output_directory>

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf. 
bedtools intersect -wa -wb \
-a mean_low_coverage_genes \
-b <PATH_to_resourses_directory>/selectionRepeatMasker | \
# Keeping selected columns.
cut -f 1,2,3,4,5,6,7,12,13,14 > genes_mean_repeat_annotation

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 genes_mean_repeat_annotation | uniq > rmdup
mv rmdup genes_mean_repeat_annotation

### Pct coverage genes	intersect

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf. 
bedtools intersect -wa -wb \
-a pct_low_coverage_genes \
-b <PATH_to_resourses_directory>/selectionRepeatMasker | \
# Keeping selected columns.
cut -f 1,2,3,4,5,6,7,12,13,14 > genes_pct_repeat_annotation

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 genes_pct_repeat_annotation | uniq > rmdup
mv rmdup genes_pct_repeat_annotation

### Mean coverage exons	intersect

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf. 
bedtools intersect -wa -wb \
-a mean_low_coverage_exons \
-b <PATH_to_resourses_directory>/selectionRepeatMasker | \
# Keeping selected columns.
cut -f 1,2,3,4,5,6,7,8,13,14,15 > exons_mean_repeat_annotaion

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 exons_mean_repeat_annotation | uniq > rmdup
mv rmdup exons_mean_repeat_annotation

### Pct coverage exons intersect

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf. 
bedtools intersect -wa -wb \
-a pct_low_coverage_exons \
-b <PATH_to_resourses_directory>/selectionRepeatMasker | \
# Keeping selected columns.
cut -f 1,2,3,4,5,6,7,8,13,14,15 > exons_pct_repeat_annotation

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 exons_pct_repeat_annotation | uniq > rmdup
mv rmdup exons_pct_repeat_annotation
