# Entering data directory. 
cd <PATH>

# for loop to iterate over each of the bed files in data directory.
for i in *.bed; do
	# cut to select specific columns in each bed file and create a temp file
	cut -f 1,2,3,5,7,12,13 "$i" > "temp_file"
	# renaming each of the temp files using their .bed file names 
	mv temp_file "$i"; done
