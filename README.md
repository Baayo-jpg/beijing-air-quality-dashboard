# Beijing Air Quality Dashboard

Dashboard interaktif untuk mengeksplorasi kualitas udara di Beijing berdasarkan data dari 12 stasiun pemantauan selama periode 2013–2017. Aplikasi dibuat dengan Python dan Streamlit.

## Fitur

- Memfilter data berdasarkan rentang tanggal dan stasiun pemantauan.
- Melihat rata-rata konsentrasi PM2.5, PM10, SO2, dan NO2.
- Melihat tren bulanan konsentrasi PM2.5.
- Membandingkan rata-rata PM2.5 antarstasiun.
- Melihat distribusi kategori kualitas udara.

## Dataset

Data mentah dari 12 stasiun tersimpan di folder `data/`. Dashboard menggunakan data gabungan yang tersedia di `dashboard/main_data.csv`. Notebook analisis tersedia di `notebook.ipynb`.

## Struktur Direktori

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   └── PRSA_Data_<nama_stasiun>_20130301-20170228.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Persyaratan

- Python 3
- pip

## Instalasi

1. Buka terminal di direktori utama proyek.
2. (Opsional) Buat dan aktifkan virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS atau Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Pasang dependensi:

   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

Pastikan terminal berada di direktori utama proyek, lalu jalankan:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka di browser. Jika tidak terbuka otomatis, kunjungi:

```text
http://localhost:8501
```

## Deployment

Dashboard yang telah di-deploy dapat diakses melalui tautan yang tercantum di [`url.txt`](url.txt).
