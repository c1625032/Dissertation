# Loading in approproate modules
module load bedtools

### Mean coverage exons intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/all_regions_output/04-repeat-annotation/total_dataframe_repeat_annotation \
-b /scratch/c.c1625032/dissertation/resources/clinvar/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > /scratch/c.c1625032/dissertation/output/all_regions_output/05-clinvar-annotation/total_dataframe_repeat_clinvar_intersection


