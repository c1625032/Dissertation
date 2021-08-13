
# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to clinvar directory is stored as an object.
clinvarDirectory = "<PATH>"

# Reading in omim file.
omim = pd.read_table("<PATH_to_resources_directory>/genemap2.txt")

# Selecting appropriate columns.
omim = omim.iloc[ : , [10] + [12]]

# Renaming columns.
omim.columns = ['Gene_ID', 'OMIM_Phenotypes']

##### Genes

### Mean coverage

# Reading in clinvar annotation file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_mean_repeat_clinvar_annotation"))

# Performing merge.
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/genes_mean_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

### Pct coverage
# Reading in clinvar annotation file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_pct_repeat_clinvar_annotation"))

# Performing merge.
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/genes_pct_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

##### Exons

### Mean coverage 
# Reading in clinvar annotation file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_mean_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/exons_mean_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

### Pct Coverage
# Reading in clinvar annotation file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_pct_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/exons_pct_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

print('Done')
