import pandas as pd


#create path to hcpcs file
hcpcs_file_path = "input/HCPC2025_OCT_ANWEB_v3.txt"

#read in hcpcs file into a data frame and to fix the fixed width formatting
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

hcpcs_df = pd.read_fwf(hcpcs_file_path, colspecs=colspecs, names=column_names)

#display the columns to see what is viable
hcpcs_df.info()

#I want to keep Code and Description1 as my columns
hcpcs_df = hcpcs_df [['Code', 'Description1']]

#add a new column to last updated
hcpcs_df['Last_Updated'] = '2025-09-10' 

#change column names to fit
hcpcs_df = hcpcs_df.rename(columns={
    'Code' : 'HCPCS_Code',
    'Description1' : 'Description',
    'Last_Updated' : 'Last_Updated'
})

#save as CVS in outputs 
output_path = 'output/csv/hcpcs_codes.csv'
hcpcs_df.to_csv(output_path, index= False)
