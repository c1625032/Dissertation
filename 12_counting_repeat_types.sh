### Mean coverage exons

# Entering output direcory.
cd <PATH>

# Cutting the repeat class column.
cut -f10 exons_mean_repeat_clinvar_omim_annotation > mean_class

# Removing header row.
sed '1d' mean_class > class_tmp

# Counting number of each type of repeat.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' class_tmp > mean_class

# Removing spare file.
rm class_tmp

### pct coverage exons

# Cutting the repeat class column.
cut -f10 exons_pct_repeat_clinvar_omim_annotation > pct_class

# Removing header row.
sed '1d' pct_class > class_tmp

# Counting number of each type of repeat.
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' class_tmp > pct_class

# Removing spare file.
rm class_tmp
