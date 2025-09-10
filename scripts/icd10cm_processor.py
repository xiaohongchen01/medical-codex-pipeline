import pandas as pd 
import re

#define the file path
file_path = "input/icd10cm_order_2025.txt"

#initialize a blank list to gold the parsed codes
codes = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:

        #remove white space and check line length
        line = line .rstrip('n\r')
        if len(line) <15:   #skip short lines
            continue

        #parse the fixed-length format based on the pdf instructions
        order_num = line[0:5].strip() #order number, first 6 characters
        code = line[6:13].strip() # ICD-10-CM code, characters 7-13
        level = line[14:15].strip() #level indictor (0 or 1), character 15

        # Parse description, and description_detailed that follows
        remaining_text = line[16:] #text after position 16

        # split by 4+ spaces to separate description and detailed description
        parts = re.split(r'\s{4,}', remaining_text, 1)

        #Extract description and detailed description
        description = parts[0].strip() if len(parts) > 0 else ''
        description_detailed = parts[1].strip() if len(parts) > 1 else ''

        #append the parsed data to the codes list
        codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed
        })

##create a dataframe from the parsed codes
icdcodesUS = pd.DataFrame(codes)

#view in the dataframe
print(icdcodesUS)

#look at the dataframe columns
print(icdcodesUS.columns)

#i like the order_num and description_detailed columns
icdcodesUS = icdcodesUS[[
    'order_num', 'description_detailed'
]]

#add last updated columnn
icdcodesUS['Last_Updated'] = '2024-06-28'

#rename and reorder columns
icdcodesUS = icdcodesUS.rename(columns={
    'order_num': 'Order Number',
    'description_detailed': 'Description',
    'Last_Updated': 'Last_Updated'
})

## save the dataframe to csv file
icdcodesUS.to_csv('output/csv/icd10cm_codes_2025.csv', index=False)
