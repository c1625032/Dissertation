# Importing modules.
# os is used to perform different opperating system tasks, sys is used to manipulate the run time environment.
import os, sys
# Pandas is a data frame manipulation module and here the as is used to create a shortcut name pd so calling the modules functions is$
import pandas as pd

##### Genes

### Mean Coverage

# Reading in file
genes_mean_file = pd.read_table("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_mean_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Mean_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Grouping repeat name column if all other columns match
genes_mean_file = genes_mean_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Mean_Coverage', 'Repeat_Class', 'Repeat_Family'], as_index=False).agg({'Repeat_Name': ','.join})

# Rearranging columns
genes_mean_file = genes_mean_file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Mean_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Exporting file
genes_mean_file.to_csv("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_mean_repeat_annotation",header=True, sep='\t', index=False)

### Pct Coverage
# Reading in file
genes_pct_file = pd.read_table("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_pct_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Pct_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Grouping repeat name column if all other columns match
genes_pct_file = genes_pct_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Pct_Coverage', 'Repeat_Class', 'Repeat_Family'], as_index=False).agg({'Repeat_Name': ','.join})

# Rearranging columns
genes_pct_file = genes_pct_file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Pct_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Exporting file
genes_pct_file.to_csv("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/genes_pct_repeat_annotation",header=True, sep='\t', index=False)

##### Exons

### Mean Coverage
# Reading in file
exons_mean_file = pd.read_table("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_mean_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Grouping repeat name column if all other columns match
exons_mean_file = exons_mean_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Exon(s)', 'Mean_Coverage', 'Repeat_Class', 'Repeat_Family'], as_index=False).agg({'Repeat_Name': ','.join})

# Rearranging columns
exons_mean_file = exons_mean_file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Mean_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Exporting file
exons_mean_file.to_csv("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_mean_repeat_annotation",header=True, sep='\t', index=False)

### Pct coverage
# Reading in file
exons_pct_file = pd.read_table("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_pct_repeat_annotation", names=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Pct_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Grouping repeat name column if all other columns match
exons_pct_file = exons_pct_file.groupby(by=['Chr', 'Start', 'End', 'Strand', 'Gene_ID', 'Gene_Name', 'Exon(s)', 'Pct_Coverage', 'Repeat_Class', 'Repeat_Family'], as_index=False).agg({'Repeat_Name': ','.join})

# Rearranging columns
exons_pct_file = exons_pct_file.reindex(columns=["Chr", "Start", "End", "Strand", "Gene_ID", "Gene_Name", "Exon(s)", "Pct_Coverage", "Repeat_Name", "Repeat_Class", "Repeat_Family"])

# Exporting file
exons_pct_file.to_csv("/scratch/c.c1625032/dissertation/output/low_coverage_outputs/04-repeat-annotation/exons_pct_repeat_annotation",header=True, sep='\t', index=False)
