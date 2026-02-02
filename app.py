import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Haryana Dashboard", layout="wide")

st.title("📊 Haryana Water Dashboard")

# Load data
compare = pd.read_csv("compare.csv")
groundwater = pd.read_csv("groundwater.csv")
gsa = pd.read_csv("gsa.csv")

# Sidebar filter
district = st.sidebar.selectbox(
    "Select District",
    compare.iloc[:,0].unique()
)

filtered = compare[compare.iloc[:,0] == district]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Rows", filtered.shape[0])
col2.metric("Columns", filtered.shape[1])
col3.metric("District", district)

st.subheader("Filtered Data")
st.dataframe(filtered)

# Chart
fig = px.bar(filtered, x=filtered.columns[0], y=filtered.columns[1])
st.plotly_chart(fig, use_container_width=True)

# Groundwater section
st.subheader("Groundwater Overview")
st.dataframe(groundwater.head())

# Download button
csv = filtered.to_csv(index=False)

st.download_button(
    "Download filtered data",
    csv,
    "filtered.csv"
)
