import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title='Beijing Air Quality Dashboard',
    page_icon='🌤️',
    layout='wide',
)


@st.cache_data
def load_data():
  df = pd.read_csv('dashboard/main_data.csv')
  df['datetime'] = pd.to_datetime(df['datetime'])
  return df


df = load_data()

# Sidebar Filters
st.sidebar.header('Filter Data Pemantauan')
min_date = df['datetime'].min().date()
max_date = df['datetime'].max().date()

start_date, end_date = st.sidebar.date_input(
    'Pilih Rentang Waktu:',
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date,
)

selected_stations = st.sidebar.multiselect(
    'Pilih Stasiun Pemantauan:',
    options=df['station'].unique(),
    default=df['station'].unique(),
)

# Filter Processing
filtered_df = df[
    (df['datetime'].dt.date >= start_date)
    & (df['datetime'].dt.date <= end_date)
    & (df['station'].isin(selected_stations))
]

# Header
st.title('🌤️ Beijing Air Quality Analytics Dashboard')
st.markdown('---')

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric('Rata-rata PM2.5', f"{filtered_df['PM2.5'].mean():.2f} µg/m³")
col2.metric('Rata-rata PM10', f"{filtered_df['PM10'].mean():.2f} µg/m³")
col3.metric('Rata-rata SO2', f"{filtered_df['SO2'].mean():.2f} µg/m³")
col4.metric('Rata-rata NO2', f"{filtered_df['NO2'].mean():.2f} µg/m³")

st.markdown('---')

# Chart 1: Monthly Trend
st.subheader('📈 Tren Konsentrasi PM2.5 Waktu ke Waktu')
monthly_filtered = (
    filtered_df.groupby(filtered_df['datetime'].dt.to_period('M'))['PM2.5']
    .mean()
    .reset_index()
)
monthly_filtered['datetime'] = monthly_filtered['datetime'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(
    monthly_filtered['datetime'],
    monthly_filtered['PM2.5'],
    color='#1f77b4',
    linewidth=2,
    marker='o',
)
ax.set_ylabel('PM2.5 (µg/m³)')
st.pyplot(fig)

# Chart 2 & 3
col_left, col_right = st.columns(2)

with col_left:
  st.subheader('📊 Rata-Rata PM2.5 per Stasiun')
  station_agg = (
      filtered_df.groupby('station')['PM2.5']
      .mean()
      .reset_index()
      .sort_values(by='PM2.5', ascending=False)
  )
  fig, ax = plt.subplots(figsize=(6, 4))
  sns.barplot(
      x='PM2.5', y='station', data=station_agg, palette='Blues_r', ax=ax
  )
  ax.set_xlabel('PM2.5 (µg/m³)')
  st.pyplot(fig)

with col_right:
  st.subheader('🏷️ Distribusi Kategori Kualitas Udara (AQI)')
  aqi_counts = filtered_df['AQI_Category'].value_counts()
  fig, ax = plt.subplots(figsize=(6, 4))
  ax.pie(
      aqi_counts,
      labels=aqi_counts.index,
      autopct='%1.1f%%',
      startangle=90,
      colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'],
  )
  st.pyplot(fig)