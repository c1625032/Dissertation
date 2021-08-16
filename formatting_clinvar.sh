# Keeping variants that are likley pathogenic or pathogenic, removing mitochondrial variants and cutting the co-ordinate of variant
grep 'Likely_pathogenic\|Pathogenic' clinvar.vcf | \
awk '$1 != "MT"' | \
cut -f 1,2 > path_only_clinvar_coordinates.vcf

# Creating an end co-orinate ready for merge by taking start co-orinate, adding it back to file and adding 1.
cut -f2 path_only_clinvar_coordinates.vcf > end_coordinate
paste -d "\t" path_only_clinvar_coordinates.vcf end_coordinate > path_only_clinvar_coordinates_plus_end.vcf
awk 'BEGIN{FS=OFS="\t"} {$3+=1}1' path_only_clinvar_coordinates_plus_end.vcf > path_only_clinvar_coordinates.bed

# Removing intermediate files
rm path_only_clinvar_coordinates_plus_end.vcf path_only_clinvar_coordinates.vcf end_coordinate
