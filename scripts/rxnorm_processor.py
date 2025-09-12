#import polars and pathlib
import polars as pl
from pathlib import Path

#direct file path
file_path = Path('input/RXNATOMARCHIVE.RRF')

#put in column names based on the file structure
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

#have polars read the file into a dataframe
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

#view the dataframe
print(df)
print(df.columns)


#very long columns so i want to see all the columns
pl.Config.set_tbl_cols(-1)  #shows all columns with no limits
pl.Config.set_tbl_rows(5) #to show only the first 5 rows
pl.Config.set_tbl_formatting("ASCII_FULL_CONDENSED") #readability
print(df.head(5))


#i like the columns "code" and "str"
df = df[['code', 'str']]

#add last updated columnn
df = df.with_columns(pl.lit('2025-08-27').alias('Last_Updated'))

#rename and relist columns
df + df.rename({
    'code' : 'RxNorm_Code',
    'str' : 'Description',
    'Last_Updated' : 'Last_Updated'
})

#put output path and save as csv
output_dir = Path('output/csv/') #specify output path
output_dir.mkdir(exist_ok=True) #makes sure output directoy exists
output_path = output_dir / 'RXNATOMACHIVE.csv' #name the output file 

df.write_csv(output_path)