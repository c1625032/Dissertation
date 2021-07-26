cd /scratch/c.c1625032/dissertation/output/all_regions_output/06-omim-annotation/
sed '1d' total_dataframe_repeat_clinvar_omim_annotation > tmp
sed -i 's/_/ /g' tmp  
sort -k1,1 -k2,2 -k3,3 tmp | uniq > total_dataframe_repeat_clinvar_omim_annotation
rm tmp
