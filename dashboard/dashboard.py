import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Data: Bike Sharing Dataset (Day)")

# Load Dataset
file_path = 'day.csv'
try:
    data = pd.read_csv(file_path)
    st.write("Data berhasil dimuat.")
except FileNotFoundError:
    st.error(f"File '{file_path}' tidak ditemukan.")
    st.stop()

# Tampilkan Dataframe
st.header("Dataset")
st.dataframe(data)

# Statistik Deskriptif
st.header("Statistik Deskriptif")
st.write(data.describe())

# Sidebar untuk Filter
st.sidebar.header("Filter Data")
st.sidebar.markdown("Gunakan filter untuk menyesuaikan data yang ditampilkan.")

# Filter Tahun
year_column = "yr"
if year_column in data.columns:
    year_options = data[year_column].unique()
    selected_year = st.sidebar.selectbox("Pilih Tahun", year_options)
    data = data[data[year_column] == selected_year]

# Filter Musim
season_column = "season"
if season_column in data.columns:
    season_options = data[season_column].unique()
    selected_season = st.sidebar.multiselect("Pilih Musim", season_options, default=season_options)
    data = data[data[season_column].isin(selected_season)]

# Visualisasi Data
st.header("Visualisasi Data")

# Line Chart: Tren Penggunaan Sepeda
st.subheader("Tren Penggunaan Sepeda")
if "dteday" in data.columns and "cnt" in data.columns:
    data["dteday"] = pd.to_datetime(data["dteday"])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x="dteday", y="cnt", ax=ax)
    plt.title("Tren Penggunaan Sepeda")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Penggunaan")
    st.pyplot(fig)
else:
    st.warning("Kolom 'dteday' atau 'cnt' tidak tersedia dalam dataset.")

# Bar Chart: Distribusi Penggunaan Berdasarkan Musim
st.subheader("Distribusi Penggunaan Berdasarkan Musim")
if season_column in data.columns and "cnt" in data.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=data, x=season_column, y="cnt", ax=ax, palette="viridis")
    plt.title("Distribusi Penggunaan Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penggunaan")
    st.pyplot(fig)
else:
    st.warning("Kolom 'season' atau 'cnt' tidak tersedia dalam dataset.")

# Histogram: Distribusi Penggunaan
st.subheader("Histogram Distribusi Penggunaan")
if "cnt" in data.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data["cnt"], bins=30, kde=True, color="blue", ax=ax)
    plt.title("Distribusi Jumlah Penggunaan")
    plt.xlabel("Jumlah Penggunaan")
    plt.ylabel("Frekuensi")
    st.pyplot(fig)
else:
    st.warning("Kolom 'cnt' tidak tersedia dalam dataset.")
