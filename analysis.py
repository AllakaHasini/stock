import pandas as pd
import os

input_dir = r"C:/Users/allak/Documents/guvi/project 2/data_csv"
output_file = r"C:/Users/allak/Documents/guvi/project 2/stock_metrics_summary.csv"

summary = []

for file in os.listdir(input_dir):
    if file.endswith(".csv"):
        filepath = os.path.join(input_dir, file)
        df = pd.read_csv(filepath)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])
        df = df.sort_values('date')
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        df = df.dropna(subset=['close'])
        df['daily_return'] = df['close'].pct_change()
        df['cumulative_return'] = (1 + df['daily_return']).cumprod() - 1

        symbol = df['symbol'].iloc[0] if 'symbol' in df.columns else file.replace('.csv', '')
        yearly_return = df['cumulative_return'].iloc[-1] if not df['cumulative_return'].empty else 0
        volatility = df['daily_return'].std() if not df['daily_return'].isnull().all() else 0

        summary.append({
            'symbol': symbol,
            'return': yearly_return,
            'volatility': volatility
        })

summary_df = pd.DataFrame(summary)
summary_df.to_csv(output_file, index=False)

print("stock_metrics_summary.csv generated successfully.")
