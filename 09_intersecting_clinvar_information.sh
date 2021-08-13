# Loading in approproate module.
module load bedtools

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf.
bedtools intersect -wa -wb \
-a <PATH_to_output_directory>/total_dataframe_repeat_annotation \
-b <PATH_to_resources>/pathogenic-only-clinvar.vcf | \
# Cutting the second column.
cut -f2 | \
# Using awk command to count the number of duplicatea and present them in an array.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH_to_output_directory>/total_dataframe_repeat_clinvar_intersection


