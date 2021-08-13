# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to data directory is stored as an object.
dataDirectory = "<PATH>"

# Creating an object of the data directory as a list.
fileNames = os.listdir(dataDirectory)

# Sorting into alphabetical and numerical order.
fileNames.sort()

# Creating a data frame from the fileNames object.
fileNamesDataframe = pd.DataFrame({'filename':fileNames})

# Creating an empty dictionary.
dataframeCollection = {}

# for loop to import each data file within the direcotry into the dataframeCollection dictionary.
# os.path.join adds the dataDirectory path to each of the file names in fileNames object.
# Skip rows is used to ignore the header row and new header names are allocated.
for filename in fileNames:
	dataframeCollection[filename] = pd.read_table(os.path.join(dataDirectory, filename), skiprows = 1, names=["Chr", "Start", "End", "mean_cvg", "median_cvg", "pct_above_15", "pct_above_30"])

##### Genes

# Reading in the gene_annotation_file.
gene_annotation_file = pd.read_table("<PATH_to_output_files>/gene_bed_file.bed", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name"])

### Gene pct above 15

# for loop to filter and merge each of the data files into a single dataframe.
# range is used to create a sequence from the file at index 0 to the last file within fileNames object using the len function.
for i in range(0, len(fileNames)):
	# if statement to start the iteration at file index 0.
	if i == 0:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.    
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in the 2nd (Start Co-ordinate) and 5th (pct above 15) column.
		file = df.iloc[:, [1] + [6]]
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]
	# An elif statement for all files with an index of one or greater.
	elif i >=1:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in 5th (pct above 15) column.
		file1 = df.iloc[:, [6]]
		# Merging files together.
		file = pd.concat([file, file1], sort=False, axis=1)
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]

# Merging large data frame with intersected gtf file based on start co-ordinates.
output = gene_annotation_file.merge(file, how='left', on='Start')

# Exporting merged dataframe.
output.to_csv("<PATH_to_output_directory>/genes_pct_above_15_dataframe.bed",header=True, sep='\t', index=False)

print('Gene percentage coverage file created')

### Gene mean coverage 

# for loop to filter and merge each of the data files into a single dataframe.
# range is used to create a sequence from the file at index 0 to the last file within fileNames object using the len function.
for i in range(0, len(fileNames)):
	# if statement to start the iteration at file index 0.
	if i == 0:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in the 2nd (Start Co-ordinate) and 5th (pct above 15) column.
		file = df.iloc[:, [1] + [3]]
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]
	# An elif statement for all files with an index of one or greater.
	elif i >=1:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in either 4th (mean coverage) column.
		file1 = df.iloc[:, [3]]
		# Merging files together.
		file = pd.concat([file, file1], sort=False, axis=1)
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]

# Merging large data frame with intersected gtf file based on start co-ordinates.
output = gene_annotation_file.merge(file, how='left', on='Start')

# Exporting merged dataframe
output.to_csv("<PATH_to_output_directory>/genes_mean_coverage_dataframe.bed",header=True, sep='\t', index=False)

print('Gene mean coverage file created')

### Exons

# Reading in the gtf intersect file.
exon_annotation_file = pd.read_table("<PATH_to_output_directory>/exon_bed_file.bed", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Exon", "Gene_Name"])

### Exon pct above 15

# for loop to filter and merge each of the data files into a single dataframe.
# range is used to create a sequence from the file at index 0 to the last file within fileNames object using the len function.
for i in range(0, len(fileNames)):
	# if statement to start the iteration at file index 0.
	if i == 0:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in the 2nd (Start Co-ordinate) and 5th (pct above 15) column.
		file = df.iloc[:, [1] + [6]]
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]
	# An elif statement for all files with an index of one or greater.
	elif i >=1:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in 5th (pct above 15) column.
		file1 = df.iloc[:, [6]]
		# Merging files together.
		file = pd.concat([file, file1], sort=False, axis=1)
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]

# Merging large data frame with intersected gtf file based on start co-ordinates.
output = exon_annotation_file.merge(file, how='left', on='Start')

# Exporting merged dataframe.
output.to_csv("<PATH_to_output_directory>/exons_pct_above_15_dataframe.bed",header=True, sep='\t', index=False)

print('Exon percentage coverage file created')

### Exon mean coverage

# for loop to filter and merge each of the data files into a single dataframe.
# range is used to create a sequence from the file at index 0 to the last file within fileNames object using the len function.
for i in range(0, len(fileNames)):	
	# if statement to start the iteration at file index 0.
	if i == 0:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in the 2nd (Start Co-ordinate) and 5th (pct above 15) column.
		file = df.iloc[:, [1] + [3]]
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]
	# An elif statement for all files with an index of one or greater.
	elif i >=1:
		# Print statement to inform user as to how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in either 4th (mean coverage) column.
		file1 = df.iloc[:, [3]]
		# Merging files together.
		file = pd.concat([file, file1], sort=False, axis=1)
		# Renaming column according to file name.
		file.columns = [*file.columns[:-1], '' + fileNames[i]]

# Merging large data frame with intersected gtf file based on start co-ordinates.
output = exon_annotation_file.merge(file, how='left', on='Start')

# Exporting merged dataframe.
output.to_csv("<PATH_to_output_directory>/exons_mean_coverage_dataframe.bed",header=True, sep='\t', index=False)

print('Exon mean coverage file created')
