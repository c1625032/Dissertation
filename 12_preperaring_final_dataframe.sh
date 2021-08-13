# Entering output directory.
cd <PATH_to_output_directory>/06-omim-annotation/
# Delete first line containing headers.
sed '1d' total_dataframe_repeat_clinvar_omim_annotation > tmp
# Remove common underscore feature.
sed -i 's/_/ /g' tmp
# Sort file and remove duplicates.
sort -k1,1 -k2,2 -k3,3 tmp | uniq > total_dataframe_repeat_clinvar_omim_annotation
# Remove temp file.
rm tmp
