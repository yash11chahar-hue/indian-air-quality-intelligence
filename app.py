import pandas as pd
import streamlit as st

st.set_page_config(page_title="Delhi PM2.5, November 2024", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("delhi_pm25_november_2024_all_stations.csv")
    df["period_start"] = pd.to_datetime(df["period_start"])
    df["station"] = df["station_name"].str.split(",").str[0]
    return df

df = load_data()

st.title("Delhi PM2.5 Pollution: November 2024")
st.write(f"{df['station'].nunique()} monitoring stations, {df['period_start'].nunique()} days.")

# Sidebar: choose which stations to show
all_stations = sorted(df["station"].unique())
selected = st.sidebar.multiselect("Choose stations", all_stations, default=all_stations)

if not selected:
    st.warning("Pick at least one station in the sidebar.")
    st.stop()

filtered = df[df["station"].isin(selected)]

# Summary table: one row per station
summary = (
    filtered.groupby("station")["mean"]
    .agg(
        monthly_average="mean",
        highest_daily_average="max",
        lowest_daily_average="min",
        days_recorded="count",
    )
    .round(2)
    .sort_values("monthly_average", ascending=False)
    .reset_index()
)

st.subheader("Summary by station")
st.caption("Monthly average = simple average of the daily averages, in µg/m³.")
st.dataframe(summary, hide_index=True)

# Chart 1: compare monthly averages
st.subheader("Monthly average PM2.5 by station")
st.bar_chart(summary.set_index("station")["monthly_average"], y_label="PM2.5 (µg/m³)")

# Chart 2: daily time series
st.subheader("Daily average PM2.5 through November 2024")
daily = filtered.pivot(index="period_start", columns="station", values="mean")
st.line_chart(daily, y_label="PM2.5 (µg/m³)")

# Table + download
st.subheader("Daily observations")
st.dataframe(filtered, hide_index=True)

csv_bytes = filtered.drop(columns=["station"]).to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download selected data as CSV",
    data=csv_bytes,
    file_name="delhi_pm25_november_2024_selected_stations.csv",
    mime="text/csv",
)

# Data and limitations
st.subheader("Data and limitations")
st.markdown(
    """
- **Source:** the India Air Quality Database API from XKDR (https://airquality.xkdr.org/), accessed from Google Colab.
- **Scope:** five selected Delhi monitoring stations (four DPCC, one IMD), PM2.5 only, 1 to 30 November 2024. These results do **not** represent all of Delhi.
- **Daily values:** each row is one station-day. `mean`, `min` and `max` summarise that day's readings, and `n` is the number of readings behind it (up to 24).
- **Incomplete days:** some days have fewer than 24 readings. The lowest count is 13 (Anand Vihar), so its daily average rests on less data than the others.
- **Monthly average:** the simple average of the 30 daily averages, not weighted by the number of readings per day.
- **Validation:** these numbers have **not** been compared against official CPCB bulletins.
"""
)