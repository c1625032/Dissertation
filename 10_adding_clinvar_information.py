# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to output directory. Can use the following commented out command.
#print(os.getcwd())

# Path to clinvar directory is stored in a variable so it is easier to refer to later.
clinvarDirectory = "<PATH>/output/all_regions_output/05-clinvar-annotation"

# Path to repeat directory is stored in a variable so it is easier to refer to later.
repeatDirectory = "<PATH>/output/all_regions_output/04-repeat-annotation"
 
# Reading in repeat annotation file
repeat = pd.read_table(os.path.join(repeatDirectory, "total_dataframe_repeat_annotation"))

# Reading in clinvar interection file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "total_dataframe_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/output/all_regions_output/05-clinvar-annotation/total_dataframe_repeat_clinvar_annotation", header=True, sep='\t', index=False)

print('Done')
