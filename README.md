# Medical Codex Pipeline

## Overview
This repository is a python pipeline for processing and analyzing medical data.

## Getting Started

```bash
# Clone the repository
 git clone https://github.com/yourusername medical-codex-pipeline.git

# Navigate into the repository folder
cd medical-codex-pipeline

#Check the status of your local repository
git status
```

### Basic Git Commands You'll Need
```bash
# Check if there are updates to download:
git pull
```
### 3. Understanding .gitignore
The `.gitignore` file is crucial for this repository because there are really large csv and datafiles here, which prevents it from being pushed into GitHub.

- **Licensing Concerns**: Some medical datasets have usage restrictions and shouldn't be publicly shared


- **Repository Performance**: Keeps the repository lightweight and fast to clone/download


- **Privacy**: Prevents accidental upload of sensitive data files

#### What We're Ignoring:
Our .gitignore specifically excludes these large medical datasets:
- `input/Loinc.csv` - LOINC laboratory codes (~50MB)
- `Minput/icd10cm_order_2025.txt` - ICD-10 diagnosis codes
- `input/icd102019syst_codes.txt` - WHO ICD-10 systematic names
- `input/HCPC2025_OCT_ANWEB_v3.txt` - HCPCS procedure codes
- `input/npidata_pfile_20050523-20250810.csv` - NPI 
- `input/RXNATOMARCHIVE.RRF` - RXNORM codes
- `input/sct2_Description_Full-en_US1000124_20250301.txt` - SNOWMED codes


### Data Sources
- Snowmed (US): https://www.nlm.nih.gov/healthit/snomedct/archive.html

- ICD-10-CM (US): https://www.cms.gov/medicare/coding-billing/icd-10-codes 

- ICD-10 (WHO): https://icdcdn.who.int/icd10/index.html 

- HCPCS (US): https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update 

- LOINC: https://loinc.org/downloads/ 

- RxNorm (US): https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html 

- NPI (US) : https://download.cms.gov/nppes/NPI_Files.html 


