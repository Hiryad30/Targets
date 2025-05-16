import streamlit as st
import pandas as pd

# Load CSV using full macOS file path
# df = pd.read_csv("Targets.csv")
data = {
    "Inspector": [
        "abhishek.bhadauriya", "kasam.ganesh", "nithin.n",
        "yadhukrishnan.pu", "k.srikanth"
    ],
    "Target Inspection in this week": [30, 33, 31, 30, 30]
}

df = pd.DataFrame(data)

# Get column names (assumes first column is category/item, second is target)
item_column = df.columns[0]
target_column = df.columns[1]

# Dropdown menu
selected_item = st.selectbox("Select an item", df[item_column])

# Display corresponding target value
target = df.loc[df[item_column] == selected_item, target_column].values[0]
st.success(f"🎯 Target Value for **{selected_item}**: {target}")
