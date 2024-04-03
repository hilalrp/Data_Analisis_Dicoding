#import library yang diperlukan
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================== #
#           LOAD DATA            #
# ============================== #

def load_hour_data():
    hour_data = pd.read_csv("../Bike-sharing-dataset/hour.csv")
    return hour_data

hour_data = load_hour_data()

def load_day_data():
    day_data = pd.read_csv("../Bike-sharing-dataset/day.csv")
    return day_data

day_data = load_day_data()

# ============================== #
#        TITLE DASHBOARD         #                   
# ============================== #
# Judul Dashboard
st.title("Bike Share Dashboard")

# ============================== #
#           SIDEBAR              #
# ============================== #
st.sidebar.title("Biodata:")
st.sidebar.markdown("**• Nama: Hilal Rosyid Putra**")
st.sidebar.markdown("**• Email: [hilalrosyidputra@gmail.com](hilalrosyidputra@gmail.com)**")
st.sidebar.markdown("**• Dicoding: [hilalrp](https://www.dicoding.com/users/hilalrp/ )**")

# ============================== #
#           VISUALIZATION        #
# ============================== #
st.sidebar.title("Dataset Bike Share")
# Menampilkan dataset
if st.sidebar.checkbox("Tampilkan Day Dataset"):
    st.subheader("Raw Day Data")
    st.write(day_data)
if st.sidebar.checkbox("Tampilkan Hour Dataset"):
    st.subheader("Raw Hour Data")
    st.write(hour_data)

# Menampilkan ringkasan statistik
if st.sidebar.checkbox("Tampilkan Statistik Ringkasan Dataset 'Day'"):
    st.subheader("Ringkasan Statistik Day Dataset")
    st.write(day_data.describe())
if st.sidebar.checkbox("Tampilkan Statistik Ringkasan Dataset 'Hour'"):
    st.subheader("Ringkasan Statistik of Hour Dataset")
    st.write(hour_data.describe())

# Dataset source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')

#Visualisasi pertanyaan 1: Bagaimana hubungan antara musim (season) dan jumlah sewa sepeda (cnt) harian? Musim mana yang menjadi peak-season sewa sepeda?
seasonal_data = day_data.groupby('season')['cnt'].mean().sort_values(ascending=False)
season_names = seasonal_data.index.map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

fig, ax = plt.subplots()
ax.bar(season_names, seasonal_data)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
ax.set_title('Hubungan Musim Terhadap Jumlah Sewa Sepeda Harian')

st.header("Hubungan Antara Musim dengan Jumlah Sewa Sepeda Harian")
st.pyplot(fig)
st.markdown("Dari visualisasi di atas dapat disimpulkan bahwa, jumlah sewa sepeda paling banyak ada pada musim gugur (Fall) dan jumlah sewa sepeda paling sedikit ada pada musim semi (Spring). Musim yang menjadi peak season yakni musim gugur (Fall).")

#Visualisasi pertanyaan 2: Bagaimana tren jumlah sewa sepeda (cnt) berdasarkan waktu, seperti bulan (mnth) atau jam (hr)?
sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth", y="cnt", data=day_data, ci=None)

plt.title("Tren Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.xticks(range(1, 13))  
plt.yticks()  

st.header("Tren Jumlah Sewa Sepeda Harian Berdasarkan Waktu")
st.subheader("Berdasarkan Bulan")
st.pyplot()

sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt", data=hour_data, ci=None)

plt.title("Tren Jumlah Sewa Sepeda Harian Berdasarkan Jam")
plt.xlabel("Jam")
plt.ylabel("Jumlah Sewa Sepeda Harian")

plt.xticks(range(0, 24))  
plt.yticks() 

st.subheader("Berdasarkan Jam")
st.pyplot()
st.markdown("Berdasarkan bulan, terjadi peningkatan jumlah peminjaman sepeda pada bulan September dan Juni. Sementara itu, jika dilihat dari jamnya, peminjaman sepeda mengalami peningkatan yang signifikan pada pukul 8 pagi, kemudian mengalami penurunan. Jumlah penyewa mencapai puncaknya pada pukul 17, dan kemudian mengalami penurunan.")

#Visualisasi pertanyaan 3: Bagaimana hubungan cuaca (weathersit) terhadap jumlah sewa sepeda (cnt)?
plt.figure(figsize=(10, 6))
sns.boxplot(x="weathersit", y="cnt", data=day_data)

plt.title("Hubungan Weathersit Terhadap Jumlah Sewa Sepeda Harian")
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")

st.header("Hubungan Cuaca Terhadap Jumlah Sewa Sepeda")
st.pyplot()
st.markdown("Boxplot menunjukkan bahwa perubahan dalam kondisi cuaca secara jelas mempengaruhi perilaku pengguna sepeda. Secara lebih rinci, observasi menunjukkan bahwa pada kondisi cuaca tertentu, khususnya cuaca cerah atau sebagian berawan (weathersit 1), terdapat perbedaan yang signifikan dalam jumlah sepeda yang disewa dibandingkan weathersit lainnya. Jumlah sewa pada cuaca cerah atau sedikit berawan lebih tinggi dibandingkan dengan weathersit lainnya.")

#Visualisasi pertanyaan 4: Bagaimana cara meningkatkan jumlah sewa sepeda yang digunakan oleh pengguna casual pada weekdays?
total_casual_by_weekday = day_data[day_data['workingday'] == 1].groupby('weekday')['casual'].sum()

labels = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(labels, total_casual_by_weekday)

ax.set_xlabel("Hari Kerja")
ax.set_ylabel("Total Jumlah Sewa Sepeda Pelanggan Casual")
ax.set_title("Jumlah Sewa Sepeda Pelanggan Casual pada Hari Kerja")

st.header("Jumlah Sewa Sepeda oleh Pelanggan Casual pada Weekdays")
st.pyplot(fig)
st.markdown("""
Strategi meningkatkan jumlah sewa sepeda yang digunakan oleh pengguna casual pada weekdays:
- Menawarkan promosi khusus pada hari-hari dengan tingkat penggunaan yang rendah, seperti Senin dan Rabu, seperti diskon eksklusif atau penawaran khusus yang hanya berlaku pada hari kerja.
- Memastikan akses mudah dan kondisi baik dari fasilitas penyewaan sepeda, seperti stasiun atau lokasi penyewaan, terutama selama hari kerja.
- Intensifkan upaya pemasaran pada hari kerja, seperti melalui iklan online yang ditujukan kepada pengguna casual pada hari kerja.
- Implementasikan program loyalitas atau penawaran diskon yang berkelanjutan bagi pengguna casual yang sering menyewa sepeda pada hari kerja.
""")

st.caption("Copyright (c) 2024")
