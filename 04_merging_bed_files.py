# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to data directory. Can use the following commented out command.
#print(os.getcwd())

# Path to data directory is stored in a variable so it is easier to refer to later.
dataDirectory = "/scratch/c.c1625032/dissertation/data"

# Path to annotated bed file
outputDirectory = "/scratch/c.c1625032/dissertation/output/annotated_bed_file.bed"
 
# Creating a list containing the names of all files within the data directory so they can be called easier.
fileNames = os.listdir(dataDirectory)

# Sorting the fileNames variable into alphabetical and numerical order.
fileNames.sort()

# Creating a data frame using the fileNames variable so they can be manipulated using the pandas module.
# Here each of the file names are being put in the column 'filename'.
fileNamesDataframe = pd.DataFrame({'filename':fileNames})

# Creating an empty dictionary where each of the files can be added to using the next command. This makes it easy to access their information.
dataframeCollection = {}

# This for loop is going to import each data file and add them to the dataframeCollection dictionary.
# In each iteration the for loop is going apply the read_table function rather than importing one at a time. 
# To find the correct file, os.path.join is joining the dataDirectory path to each of the file names in fileNames variable.
# Skip rows is used to ignore the header row in each file so columns below can be recognised individually.
for filename in fileNames:
	dataframeCollection[filename] = pd.read_table(os.path.join(dataDirectory, filename), skiprows = 1, names=["Chr", "Start", "End", "mean_cvg", "median_cvg", "pct_above_15", "pct_above_30"])

# Reading in the gtf intersect file
gtf_file = pd.read_table(outputDirectory, names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name"])

# This for loop is going to perform the filtering and merging of the data files into a single dataframe.
# In each iteration the for loop will perform the following actions on each of the data files before merging.
# First range, an inbuilt python function, is used to create a sequence from the file at index 0 to the index at the end of file names. 
# len is used to return the number of items within in a list to specify the last number in the fileNames varibale (5). 
for i in range(0, len(fileNames)):
	# A condidtional 'if' is created to specify the file at index 0, ie the first file.
	if i == 0:
		# Print statement to let the user know how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating a variable with the information contained within each data file.  
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in the 2nd (Start) and either 4th (mean coverage) or 5th (pct above 15) column
		file = df.iloc[:, [1] + [6]]
		# Renaming column according to file name
		file.columns = [*file.columns[:-1], '' + fileNames[i]]
	# An else if statement to escape the 'if' statement. Here all file with an index of one or greater are filtered using the same parameters above.
	elif i >=1:
		# Print statement to let the user know how much progress has been made.
		print('Merging file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating a variable with the information contained within each data file.
		df = dataframeCollection[list(dataframeCollection)[i]]
		# Selecting all rows in either 4th (mean coverage) or 5th (pct above 15) column
		file1 = df.iloc[:, [6]]
		# Merging files together
		file = pd.concat([file, file1], sort=False, axis=1)
		# Renaming column according to file name
		file.columns = [*file.columns[:-1], '' + fileNames[i]]

# Merging large data frame with intersected gtf file based on start co-ordinates
output = gtf_file.merge(file, how='left', on='Start')

# Exporting merged dataframe
output.to_csv("../output/pct_above_15_dataframe.bed",header=True, sep='\t', index=False)

print('Done')

	


