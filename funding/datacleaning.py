import pandas as pd
import os

csv_files = [f for f in os.listdir("F:\miniproject") if f.endswith('.csv')]
for r in csv_files:
    project_dir = os.path.dirname(__file__)
    csv_path = os.path.join(project_dir, r)
    df = pd.read_csv(csv_path)
    columns_to_drop = [0,1,2]
    df.drop(df.columns[columns_to_drop], axis=1, inplace=True)
    df.to_csv(r, index=False)
    
for r in csv_files:
    project_dir = os.path.dirname(__file__)
    csv_path = os.path.join(project_dir, r)
    df = pd.read_csv(csv_path)
    columns_to_rename = {0: 'Company', 1: 'Funding Round', 2: 'Amount', 3: 'Date'}
    df.rename(columns={df.columns[k]: v for k, v in columns_to_rename.items()}, inplace=True)
    df.to_csv('your_file_updated.csv', index=False)