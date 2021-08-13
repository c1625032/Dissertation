# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Reading in data frame file. 
file = pd.read_table("<PATH_to_output>/total_dataframe_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Percent_Coverage", "Repeat_Class"])

# Grouping repeat name column if all other columns match.
file = file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Exon(s)', 'Mean_Coverage', 'Percent_Coverage'], as_index=False).agg({'Repeat_Class': '/'.join})

# Rearranging columns.
file = file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Percent_Coverage", "Repeat_Class"])

# Exporting file.
file.to_csv("<PATH_to_output_file>/total_dataframe_repeat_annotation",header=True, sep='\t', index=False)

