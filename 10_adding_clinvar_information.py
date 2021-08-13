# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Path to clinvar directory is stored as an object.
clinvarDirectory = "<PATH>"

# Path to clinvar directory is stored as an object.
repeatDirectory = "<PATH>"

##### Genes

### Mean coverage

# Reading in repeat annotation file.
repeat = pd.read_table(os.path.join(repeatDirectory, "genes_mean_repeat_annotation"))

# Reading in clinvar interection file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_mean_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge.
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/genes_mean_repeat_clinvar_annotation", header=True, sep='\t', index=False)

### Pct coverage
# Reading in repeat annotation file.
repeat = pd.read_table(os.path.join(repeatDirectory, "genes_pct_repeat_annotation"))

# Reading in clinvar interection file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "genes_pct_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge.
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/genes_pct_repeat_clinvar_annotation", header=True, sep='\t', index=False)

##### Exons

### Mean coverage 
# Reading in repeat annotation file.
repeat = pd.read_table(os.path.join(repeatDirectory, "exons_mean_repeat_annotation"))

# Reading in clinvar interection file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_mean_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge.
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/exons_mean_repeat_clinvar_annotation", header=True, sep='\t', index=False)

### Pct Coverage
# Reading in repeat annotation file.
repeat = pd.read_table(os.path.join(repeatDirectory, "exons_pct_repeat_annotation"))

# Reading in clinvar interection file.
clinvar = pd.read_table(os.path.join(clinvarDirectory, "exons_pct_repeat_clinvar_intersection"), names=["Start", "Number_of_pathogenic_variants"])

# Performing merge.
output = repeat.merge(clinvar, how='left', on='Start')

# Exporting low coverage genes dataframe.
output.to_csv("<PATH_to_output_directory>/exons_pct_repeat_clinvar_annotation", header=True, sep='\t', index=False)

print('Done')
