import streamlit as st
import pandas as pd

st.title("🎯 Weekly Target Viewer")

# URL to your raw GitHub CSV
csv_url = "https://raw.githubusercontent.com/hiryad30/targets/main/Targets.csv"

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Failed to load CSV: {e}")
        return None

df = load_data(csv_url)

if df is not None:
    st.write("📊 Data Columns:", df.columns.tolist())
    
    if df.shape[1] >= 2:
        item_column = df.columns[0]
        target_column = df.columns[1]

        selected_item = st.selectbox("Select an item", df[item_column])

        try:
            target = df.loc[df[item_column] == selected_item, target_column].values[0]
            st.success(f"🎯 Target Value for **{selected_item}**: {target}")
        except Exception as e:
            st.error(f"Could not find target value: {e}")
    else:
        st.error("CSV does not have enough columns.")
else:
    st.stop()
