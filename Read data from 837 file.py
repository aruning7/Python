# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:28:40 2025

Python code to read data from 837 file, data will be printed in the form of dataframe

@author: Arun
"""
import pandas as pd
from datetime import datetime

# Function to parse the 837 file and return a DataFrame
def parse_837_file(file_path):
    claims_data = []

    # Open and read the 837 file
    with open(r'C:\Users\AH06408\OneDrive - Elevance Health\Desktop\Python\CHPW_Claimdata.txt', 'r') as file:
        lines = file.readlines()

    # Initialize variables to store data
    patient_name = patient_dob = patient_gender = None
    provider_name = provider_npi = diagnosis_code = None
    procedure_code = service_date = amount = None

    # Parse the file content
    for line in lines:
        segments = line.strip().split('*')
        if segments[0] == 'NM1' and segments[1] == 'IL':
            patient_name = segments[3] + ' ' + segments[4]
        elif segments[0] == 'DMG':
            patient_dob = datetime.strptime(segments[2], '%Y%m%d').date()
            patient_gender = segments[3]
        elif segments[0] == 'NM1' and segments[1] == '82':
            provider_name = segments[3] + ' ' + segments[4]
            provider_npi = segments[9]
        elif segments[0] == 'HI':
            diagnosis_code = segments[1].split(':')[1]
        elif segments[0] == 'SV1':
            procedure_code = segments[1].split(':')[1]
            amount = float(segments[2])
        elif segments[0] == 'DTP' and segments[1] == '472':
            service_date = datetime.strptime(segments[3].strip('~'), '%Y%m%d').date()
            claims_data.append([patient_name, patient_dob, patient_gender, provider_name, provider_npi, diagnosis_code, procedure_code, service_date, amount])

    # Create a DataFrame from the parsed data
    df_claims = pd.DataFrame(claims_data, columns=['Patient Name', 'Patient DOB', 'Patient Gender', 'Provider Name', 'Provider NPI', 'Diagnosis Code', 'Procedure Code', 'Service Date', 'Amount'])
    return df_claims

# Path to the 837 file
file_path = 'path_to_your_837_file.txt'

# Parse the file and print the full DataFrame
df_claims = parse_837_file(file_path)
print(df_claims.to_string())
