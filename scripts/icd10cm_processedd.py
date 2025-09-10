import pandas as pd
import re

icd_10US = pd.read_csv('output/csv/icd10cm_codes_2025.csv')
icd_10US.info()