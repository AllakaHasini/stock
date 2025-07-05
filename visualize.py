import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\allak\Documents\guvi\miniproject2\data_csv\NIFTY_50.csv')
df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace=True)
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['Close'], marker='o', linestyle='-', color='blue')
plt.title(' NIFTY 50 Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.tight_layout()
plt.show()
