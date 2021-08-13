# Importing modules.
# os is used to perform different opperating system tasks.
import os
# Pandas is a data frame manipulation module, used 'as' to refer to pandas as 'pd' later in scripts.
import pandas as pd

# Reading in exon bed file.
exon_bed_file = pd.read_table("<PATH_to_output_files>/exon_bed_file.bed", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Exon(s)", "Gene_Name"])

# Converting exons column values into strings.
exon_bed_file['Exon(s)'] = exon_bed_file['Exon(s)'].astype(str)

# Grouping the exons column together if Chr, Start, End, Strand, Gene_ID and Gene_Name match.
exon_bed_file = exon_bed_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name'], as_index=False).agg({'Exon(s)': ', '.join})

# Exporting merged file.
exon_bed_file.to_csv("<PATH_to_output_files>/exon_bed_file.bed",header=True, sep='\t', index=False)
