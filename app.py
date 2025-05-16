import streamlit as st
import pandas as pd

# Load CSV using full macOS file path
# df = pd.read_csv("Targets.csv")

csv_url = "https://raw.githubusercontent.com/hiryad30/targets/main/Targets.csv"

df = pd.read_csv(csv_url)
item_column = df.columns[0]
target_column = df.columns[1]

selected_item = st.selectbox("Select an item", df[item_column])

target = df.loc[df[item_column] == selected_item, target_column].values[0]
st.success(f"🎯 Target Value for **{selected_item}**: {target}")
