# Loading in approproate modules
module load bedtools

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the vcf.
bedtools intersect -wa -wb \
-a <PATH_to_output_directory>/genes_mean_repeat_annotation \
-b <PATH_to_resource_directory>/pathogenic-only-clinvar.vcf | \
# Cutting the second column.
cut -f2 | \
# Using awk command to count the number of duplicatea and present them in an array.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/genes_mean_repeat_clinvar_intersection

### Pct coverage genes intersect
# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the vcf.
bedtools intersect -wa -wb \
-a <PATH_to_output_directory>/genes_pct_repeat_annotation \
-b <PATH_to_resource_directory>/pathogenic-only-clinvar.vcf | \
# Cutting the second column.
cut -f2 | \
# Using awk command to count the number of duplicatea and present them in an array.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/genes_pct_repeat_clinvar_intersection

### Mean coverage exons intersect
# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the vcf.
bedtools intersect -wa -wb \
-a <PATH_to_output_directory>/exons_mean_repeat_annotation \
-b <PATH_to_resource_directory>/pathogenic-only-clinvar.vcf | \
# Cutting the second column.
cut -f2 | \
# Using awk command to count the number of duplicatea and present them in an array.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/exons_mean_repeat_clinvar_intersection

### Pct coverage exons intersect
# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the vcf.
bedtools intersect -wa -wb \
-a <PATH_to_output_directory>/exons_pct_repeat_annotation \
-b <PATH_to_resource_directory>/pathogenic-only-clinvar.vcf | \
# Cutting the second column.
cut -f2 | \
# Using awk command to count the number of duplicatea and present them in an array.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/exons_pct_repeat_clinvar_intersection

