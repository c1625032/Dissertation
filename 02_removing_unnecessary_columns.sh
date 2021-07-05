# Entering data directory 
cd /scratch/c.c1625032/dissertation/data/

# for loop to iterate over each of the bed files in directory
for i in *.bed; do
	# awk to print the columns of interest in each bed file and create a temp  
#	awk -F '\t' '{ print $1, $2, $3, $5, $7, $12, $13 }' "$i" > "temp_file"
	cut -f 1,2,3,5,7,12,13 "$i" > "temp_file"
	# renaming each of the temp files using their .bed file names 
	mv temp_file "$i"; done
