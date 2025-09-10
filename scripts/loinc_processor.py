import pandas as pd

## Input/loinc.csv to load up the LOINC codes
loinc = pd.read_csv('input/Loinc.csv')

###loinc.info() to search for the columns
loinc.info()

### checking the potential column names we want to keep: loinc_NUM, definitiondescription, LONG_COMMON_NAME to find which is the most relevant data
loinc.LOINC_NUM.describe()
loinc.DefinitionDescription.describe()
loinc.LONG_COMMON_NAME.describe()

### create smaller dataframe with only the columns we want to keep
loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]

### add column to state last updated date
loinc_small["last_updated"] = '2025-09-07'

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM' : 'Code',
    'LONG_COMMON_NAME' : 'Description',
    'last_updated' : 'Last Updated'
})

### determine location of where I want the csv file to be at
file_output_path = "output/csv/loinc_small.csv"

### export to csv with no false
loinc_small.to_csv(file_output_path, index=False)