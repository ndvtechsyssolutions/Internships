import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config("Sales Dashboard")
st.title("Sales Dashboard | USA Sales Dataset")

@st.cache_data
def load_data(uploaded):
    if uploaded:
        return pd.read_csv(uploaded)
    return pd.read_csv("sales data.csv")

uploaded = st.sidebar.file_uploader("Upload Your CSV", type=["csv"])
df = load_data(uploaded)

# Normalizing column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
st.sidebar.write("Fields:", df.columns.tolist())

# Checking for the required columns in the dataset
required = {"order_id","sales","profit","quantity","category","region","order_date"}
if not required.issubset(df.columns):
    st.error(f"Missing columns: {required - set(df.columns)}")
    st.stop()

# Preprocessing 
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df.dropna(subset=["order_date","sales","profit","quantity"], inplace=True)

# Sidebar filters
min_date, max_date = st.sidebar.date_input("Date range",
                                           value=[df.order_date.min(), df.order_date.max()])
regions = st.sidebar.multiselect("Region", df.region.unique(), default=df.region.unique())
categories = st.sidebar.multiselect("Category", df.category.unique(), default=df.category.unique())

# Apply filters
# Convert date range to datetime64[ns] for comparison
start_date = pd.to_datetime(min_date)
end_date = pd.to_datetime(max_date)

mask = (
    (df["order_date"] >= start_date) &
    (df["order_date"] <= end_date) &
    df["region"].isin(regions) &
    df["category"].isin(categories)
)

filtered = df[mask]

# Statistical Summary
st.subheader("Statistical Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", filtered.order_id.nunique())
col2.metric("Total Sales", f"${filtered.sales.sum():,.0f}")
col3.metric("Total Profit", f"${filtered.profit.sum():,.0f}")
col4.metric("Avg Profit / Order", f"${filtered.profit.sum()/filtered.order_id.nunique():.2f}")

# Charts
st.subheader("Visualizations")
tab1, tab2, tab3 = st.tabs(["Sales by Category", "Profit Over Time", "Sales Distribution"])

with tab1:
    df_category = filtered.groupby("category").sales.sum().reset_index()
    fig = px.bar(df_category, x="category", y="sales", title="Sales by Category", labels={"category": "", "sales": "Sales ($USD)"})
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    df_time = filtered.set_index("order_date").resample("M").profit.sum().reset_index()
    fig = px.line(df_time, x="order_date", y="profit", title="Monthly Profit Trend", labels={"order_date": "", "profit": "Profit"})
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    labels = filtered.region.value_counts().index
    values = filtered.region.value_counts().values
    fig = px.pie(names=labels, values=values, title="Orders by Region", labels={"names": "Region", "values": "Orders"})
    st.plotly_chart(fig, use_container_width=True)

# Map (if lat/lon exists)
if "latitude" in filtered and "longitude" in filtered:
    st.subheader("Map of Sales")
    st.map(filtered[["latitude", "longitude"]])

# Data preview & download
st.subheader("Filtered Data")
st.dataframe(filtered)
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, file_name="filtered_sales_data.csv", mime="text/csv")

