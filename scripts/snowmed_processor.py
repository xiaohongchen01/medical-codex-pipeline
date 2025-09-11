# import polars and pathlib
import polars as pl
from pathlib import Path

#get direct file path
file_path = Path('input/sct2_Description_Full-en_US1000124_20250301.txt')

#specify the column names based on the file structure
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

#view the dataframe
print(df.head(5))
print(df.columns)

#columns are too long and im not sure what is the best choice for description
pl.Config.set_tbl_cols(-1) #show all columns with no limitation
print(df.head(5))


#i like the columns "ConceptId" and "term"
df = df[['conceptId', 'term']]

#add last_updated column
df = df.with_columns(pl.lit("2025-02-11").alias('Last_Updated'))

#rename and relist columns
df = df.rename({
    'conceptId' : 'SNOWMED_Code' ,
    'term' : 'Description',
    'Last_Updated' : 'Last_Updated'
})

#put output path, directory selects a location to drop off csv in. no need to name yt
output_dir = Path('output/csv') 
output_dir.mkdir(exist_ok=True)

#name the full output file path
output_path = output_dir / 'snowmed_codes_2025.csv'

#convert to csv
df.write_csv(output_path)

#unable to upload csv to github because its too large, so im going to convert to parquet
output_path = output_dir / 'snowmed_codes_2025.parquet'
df.write_parquet(output_path)
