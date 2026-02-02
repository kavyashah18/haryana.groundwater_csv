import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Haryana Groundwater Intelligence", layout="wide")

# ---------- LOAD DATA ----------
compare = pd.read_csv("compare.csv")
groundwater = pd.read_csv("groundwater.csv")
gsa = pd.read_csv("gsa.csv")

# ---------- SIDEBAR ----------
st.sidebar.title("🔍 Filters")

district = st.sidebar.selectbox(
    "Select District",
    compare.iloc[:,0].unique()
)

# ---------- HEADER ----------
st.title("💧 Haryana Groundwater Intelligence Dashboard")
st.markdown("Real-time district analytics and water resource insights")

# ---------- FILTER ----------
filtered = compare[compare.iloc[:,0] == district]

# ---------- KPI ROW ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("District", district)
col2.metric("Rows", filtered.shape[0])
col3.metric("Columns", filtered.shape[1])
col4.metric("Total Records", len(compare))

st.divider()

# ---------- CHART SECTION ----------
st.subheader("📊 District Comparison")

fig1 = px.bar(filtered,
              x=filtered.columns[0],
              y=filtered.columns[1],
              title="District Metric Overview",
              text_auto=True)

st.plotly_chart(fig1, use_container_width=True)

# ---------- GROUNDWATER TREND ----------
st.subheader("💧 Groundwater Dataset Overview")

fig2 = px.line(groundwater,
               x=groundwater.columns[0],
               y=groundwater.columns[1],
               markers=True,
               title="Groundwater Trend")

st.plotly_chart(fig2, use_container_width=True)

# ---------- GSA CHART ----------
st.subheader("🌍 GSA Resource Analytics")

fig3 = px.scatter(gsa,
                  x=gsa.columns[0],
                  y=gsa.columns[1],
                  size=gsa.columns[1],
                  title="Resource Distribution")

st.plotly_chart(fig3, use_container_width=True)

# ---------- DATA TABLE ----------
st.subheader("📄 Filtered Dataset")
st.dataframe(filtered, use_container_width=True)

# ---------- DOWNLOAD ----------
csv = filtered.to_csv(index=False)

st.download_button(
    "⬇ Download filtered data",
    csv,
    "filtered.csv"
)

# ---------- AI INSIGHT SECTION ----------
st.subheader("🧠 Automated Insight")

st.info(
    f"District {district} shows measurable variation in groundwater indicators. "
    "Monitoring sustainable extraction and recharge planning is recommended."
)

st.success("Dashboard operational ✓")
