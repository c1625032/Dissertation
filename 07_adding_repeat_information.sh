# Loading in approproate modules
module load bedtools

# Moving into output directory
cd /scratch/c.c1625032/dissertation/output/all_regions_output/04-repeat-annotation/

### Performing intersect

# Calling bedtools intersect function and specifying it should provide all information from the original files
bedtools intersect -wa -wb \
-a /scratch/c.c1625032/dissertation/output/all_regions_output/03-calculating_average_coverage/total_dataframe \
-b /scratch/c.c1625032/dissertation/resources/ucsc/selectionRepeatMasker | \
# Keeping selected columns
cut -f 1,2,3,4,5,6,7,8,9,15 > /scratch/c.c1625032/dissertation/output/all_regions_output/04-repeat-annotation/total_dataframe_repeat_annotation

# Removing duplicate lines following sorting
sort -k1,1 -k2,2 -k3,3 total_dataframe_repeat_annotation | uniq > rmdup
mv rmdup total_dataframe_repeat_annotation

