# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is$
import pandas as pd

# Reading in exon bed file
exon_bed_file = pd.read_table("/scratch/c.c1625032/dissertation/output/01-gtf-annotation/exon_bed_file.bed", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Exon(s)", "Gene_Name"])

# Converting exons column values into a string
exon_bed_file['Exon(s)'] = exon_bed_file['Exon(s)'].astype(str)

# Grouping the exons column together if Chr, Start, End, Strand, Gene_ID and Gene_Name match
exon_bed_file = exon_bed_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name'], as_index=False).agg({'Exon(s)': ', '.join})

# Exporting merged file
exon_bed_file.to_csv("/scratch/c.c1625032/dissertation/output/01-gtf-annotation/exon_bed_file.bed",header=True, sep='\t', index=False)
