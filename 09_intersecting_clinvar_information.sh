# Loading in approproate modules
module load bedtools

### Mean coverage genes intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/genes_mean_repeat_annotation \
-b <PATH>/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/genes_mean_repeat_clinvar_intersection

### Pct coverage genes intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/genes_pct_repeat_annotation \
-b <PATH>/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/genes_pct_repeat_clinvar_intersection

### Mean coverage exons intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/exons_mean_repeat_annotation \
-b <PATH>/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/exons_mean_repeat_clinvar_intersection

### Pct coverage exons intersect
# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a <PATH>/exons_pct_repeat_annotation \
-b <PATH>/pathogenic-only-clinvar.vcf | \
cut -f2 | \
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' > <PATH>/exons_pct_repeat_clinvar_intersection

