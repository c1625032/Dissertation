# Loading in approproate modules
module load bedtools

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files 
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_regions/mean_low_coverage_genes \
-b /scratch/c.c1625032/dissertation/resources/ucsc/selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,12,13,14 > /scratch/c.c1625032/dissertation/output/repeatIntersect/genes_mean_repeat_intersect

### Pct coverage genes	intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_regions/pct_low_coverage_genes \
-b /scratch/c.c1625032/dissertation/resources/ucsc/selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,12,13,14 > /scratch/c.c1625032/dissertation/output/repeatIntersect/genes_pct_repeat_intersect

### Mean coverage exons	intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_regions/mean_low_coverage_exons \
-b /scratch/c.c1625032/dissertation/resources/ucsc/selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,8,13,14,15 > /scratch/c.c1625032/dissertation/output/repeatIntersect/exons_mean_repeat_intersect

### Pct coverage exons intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_regions/pct_low_coverage_exons \
-b /scratch/c.c1625032/dissertation/resources/ucsc/selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,8,13,14,15 > /scratch/c.c1625032/dissertation/output/repeatIntersect/exons_pct_repeat_intersect
