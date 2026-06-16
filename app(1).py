
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nassau Candy Profitability Dashboard", layout="wide")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("Cleaned_Candy_Data.csv")
    except:
        return pd.read_csv("Candy.csv")

df = load_data()

df["Gross Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100
df["Profit Per Unit"] = df["Gross Profit"] / df["Units"]

st.title("Nassau Candy Distributor Dashboard")

division = st.sidebar.multiselect(
    "Division",
    df["Division"].dropna().unique(),
    default=df["Division"].dropna().unique()
)

df = df[df["Division"].isin(division)]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Revenue", f"${df['Sales'].sum():,.0f}")
c2.metric("Profit", f"${df['Gross Profit'].sum():,.0f}")
c3.metric("Margin %", f"{(df['Gross Profit'].sum()/df['Sales'].sum())*100:.2f}%")
c4.metric("Units", f"{df['Units'].sum():,.0f}")

product = df.groupby("Product Name", as_index=False)["Gross Profit"].sum()
st.plotly_chart(
    px.bar(product.sort_values("Gross Profit", ascending=False),
           x="Product Name", y="Gross Profit",
           title="Product Profitability"),
    use_container_width=True
)
