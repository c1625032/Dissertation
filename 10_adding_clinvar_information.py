# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is easier.
import pandas as pd

# User needs to enter path to output directory. Can use the following commented out command.
#print(os.getcwd())

# Path to clinvar directory is stored in a variable so it is easier to refer to later.
clinvarDirectory = "<PATH>/05-clinvar-annotation"

# Path to repeat directory is stored in a variable so it is easier to refer to later.
repeatDirectory = "<PATH>/04-repeat-annotation"

##### Genes

### Mean coverage

# Reading in repeat annotation file
repeat = pd.read_table(os.path.join(repeatDirectory, "genes_mean_repeat_annotation"))

# Reading in clinvar interection file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_mean_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/genes_mean_repeat_clinvar_annotation", header=True, sep='\t', index=False)

### Pct coverage
# Reading in repeat annotation file
repeat = pd.read_table(os.path.join(repeatDirectory, "genes_pct_repeat_annotation"))

# Reading in clinvar interection file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_pct_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/genes_pct_repeat_clinvar_annotation", header=True, sep='\t', index=False)

##### Exons

### Mean coverage 
# Reading in repeat annotation file
repeat = pd.read_table(os.path.join(repeatDirectory, "exons_mean_repeat_annotation"))

# Reading in clinvar interection file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_mean_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/exons_mean_repeat_clinvar_annotation", header=True, sep='\t', index=False)

### Pct Coverage
# Reading in repeat annotation file
repeat = pd.read_table(os.path.join(repeatDirectory, "exons_pct_repeat_annotation"))

# Reading in clinvar interection file
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_pct_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe
output.to_csv("<PATH>/exons_pct_repeat_clinvar_annotation", header=True, sep='\t', index=False)

print('Done')
