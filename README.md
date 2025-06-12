
# 🌊 FloodSight Inference - Prediksi Risiko Banjir Jabodetabek

Aplikasi web interaktif untuk memprediksi risiko banjir berdasarkan lokasi yang dipilih pengguna di peta, bulan, dan tahun. Sistem ini menggunakan model AI yang telah dideploy via API, dan fokus pada inference sederhana untuk mendukung pengambilan keputusan berbasis spasial.

🚀 **Live App:**  
👉 [https://inference-floodsight-ebz2q4rxcqgrurxu76stnl.streamlit.app/](https://inference-floodsight-ebz2q4rxcqgrurxu76stnl.streamlit.app/)

---

## 🔧 Fitur Utama

- 🌍 Peta interaktif untuk memilih lokasi (klik)
- 📍 Validasi lokasi hanya dalam wilayah Jabodetabek
- 📆 Input bulan dan tahun prediksi
- 🧠 Menggunakan model AI banjir via API eksternal
- ✅ Hasil ditampilkan jelas dengan metadata lokasi dan tahun citra

---

## 📦 Instalasi Lokal

1. Clone repo ini:
   ```bash
   git clone https://github.com/namamu/floodsight-inference.git
   cd floodsight-inference
   ```

2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

---

## 🔗 API Endpoint

Aplikasi ini menggunakan API model dari:
```
https://deploy-model-floodsight-production.up.railway.app/predict
```

Contoh query:
```
?year=2024&month=3&longitude=107.2086&latitude=-6.2915
```

---

## 📁 Struktur File

```
├── app.py               # Aplikasi utama Streamlit
└── requirements.txt     # Daftar dependensi Python
```

---

## 🗺️ Area Cakupan

Saat ini aplikasi hanya mendukung prediksi untuk wilayah:
- Jakarta
- Bogor
- Depok
- Tangerang
- Bekasi

---

## 📃 Lisensi

Proyek ini bebas digunakan untuk tujuan edukatif dan pengembangan internal. Silakan hubungi kami untuk kerja sama lebih lanjut.

---

## 🤝 Kontribusi

Pull request, masukan, atau laporan bug sangat dihargai! Silakan fork dan kembangkan.
