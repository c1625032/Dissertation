# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to output directory. Can use the following commented out command.
#print(os.getcwd())

# Path to output directory is stored in a variable so it is easier to refer to later.
outputDirectory = "<PATH>/02-merging-bed-files"

### Mean coverage 

# Reading in mean coverage file
mean = pd.read_table(os.path.join(outputDirectory, "exons_mean_coverage_dataframe.bed"))

# Calculating mean coverage values by creating a new column
mean['Mean_Coverage'] = mean.iloc[:, 7:168].mean(axis=1)

# Selecting columns for final data drame
mean = mean.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [6] + [-1]]

### Pct Coverage

# Reading in above 15 pct file
pct = pd.read_table(os.path.join(outputDirectory, "exons_pct_above_15_dataframe.bed"))

# Calculating mean coverage values by creating a new column
pct['Coverage_above_15_pct'] = pct.iloc[:, 7:168].mean(axis=1)

# Selecting columns for final data drame
pct = pct.iloc[:, [1] + [-1]]

### Merging dataframes

# Performing merge
output = mean.merge(pct, how='left', on='Start')

# Exporting dataframe
output.to_csv("<PATH>/output/all_regions_output/03-calculating_average_coverage/total_dataframe", header=True, sep='\t', index=False)

print('Done')
