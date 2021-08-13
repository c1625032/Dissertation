# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# User can use the following commented out command to find current working directory.
#print(os.getcwd())

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
for filename in fileNames:
	dataframeCollection[filename] = pd.read_table(os.path.join(dataDirectory, filename))

# for loop to filter and merge each of the data files into a single dataframe.
# range is used to create a sequence from the file at index 0 to the last file within fileNames object using the len function.
for i in range(0, len(fileNames)):
	# if statement to start the iteration at file index 0.
	if i == 0:
		# Print statement to inform user as to how much progress has been made.
		print('Running file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.  
		file = dataframeCollection[list(dataframeCollection)[i]]
		# Second if to remove file if mean coverage comes below x20 thesehold. 
		if file.iloc[ : , 4].mean() < 20:
			# Creating an object of the path and file name to be deleted.
			name = os.path.join(dataDirectory, fileNames[i])
			# Printing which file will be deleted.
			print('File: ' + fileNames[i] + ' deleted')
			# Removing file	from directory.
			os.remove(name)
	# An elif statement for all files with an index of one or greater.
	elif i >=1:
		# Print statement to inform user as to how much progress has been made.
		print('Running file ' + str(i + 1) + ' out of ' + str(len(fileNames)) + '.')
		# Creating an object containing the information of each file.
		file = dataframeCollection[list(dataframeCollection)[i]]
		# Second if to remove file if mean coverage comes below x20 thesehold.
		if file.iloc[ : , 4].mean() < 20:
			# Creating an object of the path and file name to be deleted.
			name = os.path.join(dataDirectory, fileNames[i])
			# Printing which file will be deleted.
			print('File: ' + fileNames[i] + ' deleted')
			# Removing file from directory.
			os.remove(name)

print('Done')

	


