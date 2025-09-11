## import input/icd102019syst_codes.txt file as pandas df

import pandas as pd

#file path
file_path = 'input/icd102019syst_codes.txt'

#specify the column names based on the file structure
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']


#read the file into a pandas dataframe
df = pd.read_csv(file_path, sep=';', header=None, names=columns)


#view the dataframe
print(df)
print(df.columns)


pd.set_option('display.max_columns', None) #i want to see all the columns to see what best matches
print(df)


#I like the columns "icd10_code" and "detailed_title"
df = df[['icd10_code', 'detailed_title']]

#add last updated column
df['Last_Updated'] = '2020-10-13'

#rename and relist columns
df = df.rename(columns={
    'icd10_code' : 'ICD-10-WHO_Code',
    'detailed_title' : 'Description',
    'Last_Updated' : 'Last_Updated'
})

#put output path and save as csv
output_path = 'output/csv/icd102019syst_codes.csv'
df.to_csv(output_path, index=False)




