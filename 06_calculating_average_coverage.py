# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to output directory is stored as an object.
outputDirectory = "<PATH_to_output_directory>"

### Mean coverage 

# Reading in mean coverage file.
mean = pd.read_table(os.path.join(outputDirectory, "exons_mean_coverage_dataframe.bed"))

# Calculating mean coverage values by creating a new column.
mean['Mean_Coverage'] = mean.iloc[:, 7:168].mean(axis=1)

# Selecting columns for final data frame.
mean = mean.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [6] + [-1]]

### Pct Coverage

# Reading in above 15 pct file.
pct = pd.read_table(os.path.join(outputDirectory, "exons_pct_above_15_dataframe.bed"))

# Calculating mean above 15 pct values by creating a new column.
pct['Coverage_above_15_pct'] = pct.iloc[:, 7:168].mean(axis=1)

# Selecting columns for final data frame.
pct = pct.iloc[:, [1] + [-1]]

### Merging dataframes

# Merging files
output = mean.merge(pct, how='left', on='Start')

# Exporting dataframe.
output.to_csv("<PATH_to_output_directory>/03-calculating_average_coverage/total_dataframe", header=True, sep='\t', index=False)

print('Done')
