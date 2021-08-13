# Loading in approproate modules.
module load bedtools

# Moving into output directory.
cd <PATH_to_output_directory>/04-repeat-annotation/

### Performing intersect.

# Calling bedtools intersect function and specifying opton to keep all information from the original file and add intersecticing information from the gtf.
bedtools intersect -wa -wb \
-a total_dataframe \
-b <PATH_to_resource_directory>/selectionRepeatMasker | \
# Keeping selected columns.
cut -f 1,2,3,4,5,6,7,8,9,15 > total_dataframe_repeat_annotation

# Removing duplicate lines following sorting.
sort -k1,1 -k2,2 -k3,3 total_dataframe_repeat_annotation | uniq > rmdup
mv rmdup total_dataframe_repeat_annotation

