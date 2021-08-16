# Remove header in original file
sed '1d' RepeatMasker > tmp

# Selecting the chromosome, start and end co-ordinates, strand and the repeat names, classes and families
cut -f6,7,8,10,11,12,13 tmp > selectionRepeatMasker

# Removing chr in front of chr
sed -i 's/chr//g' selectionRepeatMasker

# Remove tmp file
rm tmp
