# Loading in approproate modules
module load bedtools

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_mean_repeat_annotation \
-b /scratch/c.c1625032/dissertation/resources/clinvar/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > /scratch/c.c1625032/dissertation/output/low_coverage_outputs/05-clinvar-annotation/genes_mean_repeat_clinvar_intersection

### Pct coverage genes intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_pct_repeat_annotation \
-b /scratch/c.c1625032/dissertation/resources/clinvar/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > /scratch/c.c1625032/dissertation/output/low_coverage_outputs/05-clinvar-annotation/genes_pct_repeat_clinvar_intersection

### Mean coverage exons intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_mean_repeat_annotation \
-b /scratch/c.c1625032/dissertation/resources/clinvar/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > /scratch/c.c1625032/dissertation/output/low_coverage_outputs/05-clinvar-annotation/exons_mean_repeat_clinvar_intersection

### Pct coverage exons intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_pct_repeat_annotation \
-b /scratch/c.c1625032/dissertation/resources/clinvar/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > /scratch/c.c1625032/dissertation/output/low_coverage_outputs/05-clinvar-annotation/exons_pct_repeat_clinvar_intersection

