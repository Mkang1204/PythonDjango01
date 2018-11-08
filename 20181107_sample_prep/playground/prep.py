import pandas as pd
import csv


# the variable start is where the SampleID and Index7, Index5 headers start
# used for exporting the dataframe to prepare new SampleSheet
start = 10
# file = '/Users/marjoriekang/Box/NGS_DB/RNAseq_DB/testNGS/20181107_sample_prep/playground/SampleSheetUsed.csv'
file = '/Users/mkh1805/Box/NGS_DB/RNAseq_DB/testNGS/20181107_sample_prep/playground/SampleSheetUsed.csv'
df = pd.read_csv(file, error_bad_lines=False, sep = '\t')
print(df[0,])

dfnew = df[start:len(df)]

