# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to clinvar directory is stored as an object.
clinvarDirectory = "<PATH>/output/all_regions_output/05-clinvar-annotation/"

# Reading in omim file
omim = pd.read_table("<PATH_to_resources_directory>/genemap2.txt")

# Selecting appropriate columns.
omim = omim.iloc[ : , [10] + [12]]

# Renaming columns.
omim.columns = ['Gene_ID', 'OMIM_Phenotypes']

# Reading in clinvar annotation file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "total_dataframe_repeat_clinvar_annotation"))

# Performing merge.
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH_to_output_directory>/total_dataframe_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

print('Done')
