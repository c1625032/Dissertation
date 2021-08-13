# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to data directory is stored as an object.
outputDirectory = "<PATH>"

##### Genes

### Mean coverage

# Reading in mean coverage file.
mean_coverage_dataframe = pd.read_table(os.path.join(outputDirectory, "genes_mean_coverage_dataframe.bed"))

# Calculating mean coverage values by creating a new column.
mean_coverage_dataframe['Mean_Coverage'] = mean_coverage_dataframe.iloc[:, 6:167].mean(axis=1)

# Creating series object (True and False statements) regarding whether each row meets conditions.
underThresehold = mean_coverage_dataframe[ mean_coverage_dataframe['Mean_Coverage'] > 10 ].index

# Dropping columns from original dataframe that don't meet the thresehold.
mean_coverage_dataframe.drop(underThresehold, inplace=True)

# Selecting columns for final data drame.
mean_low_coverage_genes = mean_coverage_dataframe.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [-1]]

# Exporting low coverage genes dataframe.
mean_low_coverage_genes.to_csv("<PATH_to_output_directory>/mean_low_coverage_genes", header=True, sep='\t', index=False)

### Pct coverage

# Reading in above 15 pct file.
above_15_pct_dataframe = pd.read_table(os.path.join(outputDirectory, "genes_pct_above_15_dataframe.bed"))

# Calculating mean coverage values by creating a new column.
above_15_pct_dataframe['Coverage_above_15_pct'] = above_15_pct_dataframe.iloc[:, 6:167].mean(axis=1)

# Creating series object (True and False statements) regarding whether each row meets conditions.
underThresehold = above_15_pct_dataframe[ above_15_pct_dataframe['Coverage_above_15_pct'] > 90 ].index

# Dropping columns from original dataframe that don't meet the thresehold.
above_15_pct_dataframe.drop(underThresehold, inplace=True)

# Selecting columns for final data drame.
pct_low_coverage_genes = above_15_pct_dataframe.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [-1]]

# Exporting low coverage genes dataframe.
pct_low_coverage_genes.to_csv("<PATH_to_output_directory>/pct_low_coverage_genes", header=True, sep='\t', index=False)

##### Exons

### Mean coverage 

# Reading in mean coverage file.
mean_coverage_dataframe = pd.read_table(os.path.join(outputDirectory, "exons_mean_coverage_dataframe.bed"))

# Calculating mean coverage values by creating a new column.
mean_coverage_dataframe['Mean_Coverage'] = mean_coverage_dataframe.iloc[:, 7:168].mean(axis=1)

# Creating series object (True and False statements) regarding whether each row meets conditions.
underThresehold = mean_coverage_dataframe[ mean_coverage_dataframe['Mean_Coverage'] > 10 ].index

# Dropping columns from original dataframe that don't meet the thresehold.
mean_coverage_dataframe.drop(underThresehold, inplace=True)

# Selecting columns for final data drame.
mean_low_coverage_genes = mean_coverage_dataframe.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [6] + [-1]]

# Exporting low coverage genes dataframe.
mean_low_coverage_genes.to_csv("<PATH_to_output_directory>/mean_low_coverage_exons", header=True, sep='\t', index=False)

### Pct Coverage

# Reading in above 15 pct file.
above_15_pct_dataframe = pd.read_table(os.path.join(outputDirectory, "exons_pct_above_15_dataframe.bed"))

# Calculating mean coverage values by creating a new column.
above_15_pct_dataframe['Coverage_above_15_pct'] = above_15_pct_dataframe.iloc[:, 7:168].mean(axis=1)

# Creating series object (True and False statements) regarding whether each row meets conditions.
underThresehold = above_15_pct_dataframe[ above_15_pct_dataframe['Coverage_above_15_pct'] > 90 ].index

# Dropping columns from original dataframe that don't meet the thresehold.
above_15_pct_dataframe.drop(underThresehold, inplace=True)

# Selecting columns for final data drame.
pct_low_coverage_genes = above_15_pct_dataframe.iloc[:, [0] + [1] + [2] + [3] + [4] + [5] + [6] + [-1]]

# Exporting low coverage genes dataframe.
pct_low_coverage_genes.to_csv("<PATH_to_output_directory>/pct_low_coverage_exons", header=True, sep='\t', index=False)

print('Done')


