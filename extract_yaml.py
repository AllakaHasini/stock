import os
import yaml
import pandas as pd

input_dir = r'C:\Users\allak\Documents\guvi\miniproject2\data_yaml'
output_csv = r'C:\Users\allak\Documents\guvi\miniproject2\data_csv\NIFTY_50.csv'
records = []

for file in os.listdir(input_dir):
    if file.endswith('.yaml'):
        with open(os.path.join(input_dir, file), 'r') as f:
            month_data = yaml.safe_load(f)

        for date, data in month_data.items():
            flat_record = {'date': date}
            flat_record.update(data[0])  # since data is a list with one dict
            records.append(flat_record)

df = pd.DataFrame(records)
df.to_csv(output_csv, index=False)
print("NIFTY 50 index data extracted and saved to NIFTY_50.csv")
