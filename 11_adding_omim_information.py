# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to output directory. Can use the following commented out command.
#print(os.getcwd())

# Path to clinvar directory is stored in a variable so it is easier to refer to later.
clinvarDirectory = "<PATH>/05-clinvar-annotation"

# Reading in omim file
omim = pd.read_table("<PATH>/genemap2.txt")

# Selecting appropriate columns
omim = omim.iloc[ : , [10] + [12]]

# Renaming columns
omim.columns = ['Gene_ID', 'OMIM_Phenotypes']

##### Genes

### Mean coverage

# Reading in clinvar annotation file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_mean_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/genes_mean_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

### Pct coverage
# Reading in clinvar annotation file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_pct_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/genes_pct_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

##### Exons

### Mean coverage 
# Reading in clinvar annotation file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_mean_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/exons_mean_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

### Pct Coverage
# Reading in clinvar annotation file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_pct_repeat_clinvar_annotation"))

# Performing merge
output = clinvar.merge(omim, how='left', on='Gene_ID')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/exons_pct_repeat_clinvar_omim_annotation", header=True, sep='\t', index=False)

print('Done')
