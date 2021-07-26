# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to output directory. Can use the following commented out command.
#print(os.getcwd())

# Path to clinvar directory is stored in a variable so it is easier to refer to later.
clinvarDirectory = "<PATH>/output/all_regions_output/05-clinvar-annotation/"

# Reading in omim file
omim = pd.read_table("<PATH>/resources/omim/genemap2.txt")

# Selecting appropriate columns
omim = omim.iloc[ : , [10] + [12]]

# Renaming columns
omim.columns = ['Gene_ID', 'OMIM_Phenotypes']

##### Exons

### Mean coverage 
# Reading in clinvar annotation file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "total_dataframe_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/output/all_regions_output/06-omim-annotation/total_dataframe_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

print('Done')
