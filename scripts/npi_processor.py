#import polars and pandas
import polars as pl
import pandas as pd

#define where npi file is located
npi_file_path = 'input/npidata_pfile_20050523-20250810.csv'

#read npi files with polars because it is a larger database for pandas with small rows to see what the columns are
df_polars = pl.read_csv(npi_file_path, n_rows=1_000_000)

#use print to see the columns
print(df_polars.columns) 

#selecting columns for smaller dataframe
df_polars_small = df_polars.select(['NPI', 'Provider Last Name (Legal Name)'])

#adding column to small dataframe
df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-10').alias('Last_Updated')
)


#rename columns to match other dataframes
df_polars_small = df_polars_small.rename({
    'NPI' : 'NPI code',
    'Provider Last Name (Legal Name)' : "Provider Last Name",
    'Last_Updated' : 'Last_Updated'
})

#save as csv file
output_file_path = 'output/csv/npi_small.csv'

df_polars_small.write_csv(output_file_path)