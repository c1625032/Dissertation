# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is$
import pandas as pd

# Reading in file
file = pd.read_table("<PATH>/output/all_regions_output/04-repeat-annotation/total_dataframe_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Percent_Coverage", "Repeat_Class"])

# Grouping repeat name column if all other columns match
file = file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Exon(s)', 'Mean_Coverage', 'Percent_Coverage'], as_index=False).agg({'Repeat_Class': '/'.join})

# Rearranging columns
file = file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Percent_Coverage", "Repeat_Class"])

# Exporting file
file.to_csv("<PATH>/output/all_regions_output/04-repeat-annotation/total_dataframe_repeat_annotation",header=True, sep='\t', index=False)

