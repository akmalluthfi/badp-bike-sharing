import pandas as pd
import seaborn as sns
import streamlit as st
import plot

st.set_page_config(page_title="Bike Sharing System", page_icon=":bike:", layout="wide")
sns.set_palette("pastel")

st.title("Bike Sharing System")

df = pd.read_csv("./data/hour.csv")
df.drop("instant", axis=1, inplace=True)
df["dteday"] = pd.to_datetime(df["dteday"])

# Row 1
col1, col2, col3 = st.columns(3)
col1.metric("Casual Users", format(df["casual"].sum(), ","))
col2.metric("Registered Users", format(df["registered"].sum(), ","))
col3.metric("Total Users", format(df["cnt"].sum(), ","))

# Row 2
st.subheader("Jumlah Penyewa Tertinggi dan Terendah")
groupby_day_df = df.groupby("dteday")["cnt"].sum().reset_index()
groupby_day_df["dteday"] = groupby_day_df["dteday"].astype(str)
st.pyplot(plot.question3(groupby_day_df))

# Row 3
st.subheader("Jumlah Total Penyewa per Bulan")
df["month"] = df["dteday"].dt.to_period("M")
monthly_data = df.groupby("month")["cnt"].sum().reset_index()
monthly_data["month"] = monthly_data["month"].dt.to_timestamp()
st.pyplot(plot.question4(monthly_data))

# Row 4
st.subheader("Distribusi Penyewa Sepeda")
col1, col2 = st.columns(2)
with col1:
    mnth_df = df.groupby("mnth").agg({"casual": "sum", "registered": "sum"})
    mnth_df.reset_index(inplace=True)
    mnth_df["mnth"] = pd.to_datetime(mnth_df["mnth"], format="%m").dt.strftime("%B")

    st.pyplot(plot.question5a(mnth_df))

with col2:
    weekday_df = df.groupby("weekday").agg({"casual": "sum", "registered": "sum"})
    weekday_df.reset_index(inplace=True)

    st.pyplot(plot.question5b(weekday_df))

# Row 6
hour_df = df.groupby("hr").agg({"casual": "sum", "registered": "sum"}).reset_index()
st.pyplot(plot.question5c(hour_df))

# Row 7
col1, col2 = st.columns(2)
with col1:
    season_df = df.groupby("season").agg({"casual": "sum", "registered": "sum"})
    season_df.reset_index(inplace=True)
    st.pyplot(plot.question5d(season_df))

with col2:
    weathersit_df = df.groupby("weathersit").agg({"casual": "sum", "registered": "sum"})
    weathersit_df.reset_index(inplace=True)
    st.pyplot(plot.question5e(weathersit_df))


# Row 8
st.subheader("Time Series Decomposition")
time_series_df = df.groupby("dteday")["cnt"].sum().reset_index()
time_series_df = time_series_df.set_index("dteday")
st.pyplot(plot.time_series_decomposition(time_series_df))
