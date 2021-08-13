# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd


# Path to clinvar directory is stored as an object.
clinvarDirectory = "<PATH_to_output_directory>"

# Path to repeat directory is stored as an object.
repeatDirectory = "<PATH_to_output_directory>"
 
# Reading in repeat annotation file.
repeat = pd.read_table(os.path.join(repeatDirectory, "total_dataframe_repeat_annotation"))

# Reading in clinvar intersection file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "total_dataframe_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge.
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting file.
output.to_csv("<PATH_to_output_directory>/total_dataframe_repeat_clinvar_annotation", header=True, sep='\t', index=False)

print('Done')
