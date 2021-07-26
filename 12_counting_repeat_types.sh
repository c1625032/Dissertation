### Mean coverage exons

# Entering direcory
cd <PATH>/06-omim-annotation

# Cutting the repeat columns
cut -f10 exons_mean_repeat_clinvar_omim_annotation > mean_class
cut -f11 exons_mean_repeat_clinvar_omim_annotation > mean_family

# Removing header row
sed '1d' mean_class > class_tmp
sed '1d' mean_family > family_tmp

# Counting number of each type of repeat
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' class_tmp > mean_class
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' family_tmp > mean_family

# Removing spare files
rm class_tmp family_tmp 

### pct coverage exons

# Cutting the repeat columns
cut -f10 exons_pct_repeat_clinvar_omim_annotation > pct_class
cut -f11 exons_pct_repeat_clinvar_omim_annotation > pct_family

# Removing header row
sed '1d' pct_class > class_tmp
sed '1d' pct_family > family_tmp

# Counting number of each type of repeat
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' class_tmp > pct_class
awk 'BEGIN{FS=OFS="\t"} {arr[$0]++} END{for(i in arr){print i,arr[i]}}' family_tmp > pct_family

# Removing spare files
rm class_tmp family_tmp
