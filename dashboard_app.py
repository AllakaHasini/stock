import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("NIFTY 50 Index Dashboard")

data_folder = "data_csv"

if not os.path.exists(data_folder):
    st.error(f"Data folder '{data_folder}' not found. Please add the folder with CSV files.")
else:
    csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

    if not csv_files:
        st.error(f"No CSV files found in the folder '{data_folder}'. Please add CSV files.")
    else:
        selected_file = st.selectbox("Select a stock/index CSV file", csv_files)
        file_path = os.path.join(data_folder, selected_file)
        df = pd.read_csv(file_path)

        if 'date' not in df.columns or 'Close' not in df.columns:
            st.error("The selected file must contain 'date' and 'Close' columns.")
        else:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
            df.dropna(subset=['date', 'Close'], inplace=True)
            df.sort_values('date', inplace=True)

            st.subheader("Closing Price Over Time")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(df['date'], df['Close'], marker='o', linestyle='-')
            ax.set_title(f"Closing Price of {selected_file}")
            ax.set_xlabel("Date")
            ax.set_ylabel("Close Price")
            ax.grid(True)
            st.pyplot(fig)

