import streamlit as st
from streamlit_folium import st_folium
import folium
import requests

# Batas wilayah kasar Jabodetabek
JABODETABEK_BOUNDS = {
    "lat_min": -6.8,
    "lat_max": -5.7,
    "lon_min": 106.0,
    "lon_max": 107.2
}

def is_within_jabodetabek(lat, lon):
    return (JABODETABEK_BOUNDS["lat_min"] <= lat <= JABODETABEK_BOUNDS["lat_max"] and
            JABODETABEK_BOUNDS["lon_min"] <= lon <= JABODETABEK_BOUNDS["lon_max"])

# Konfigurasi Streamlit
st.set_page_config(page_title="Prediksi Banjir Jabodetabek", layout="wide")
st.title("🌊 Peta Prediksi Banjir")

# Buat dua kolom
col1, col2 = st.columns([2, 1])

# ========================
# KOLOM 1: PETA
# ========================
with col1:
    st.markdown("### Pilih Lokasi di Peta")
    
    # Inisialisasi peta
    m = folium.Map(location=[-6.2, 106.8], zoom_start=10)
    m.add_child(folium.LatLngPopup())  # Menampilkan lat/lon saat klik

    # Tampilkan peta interaktif
    map_data = st_folium(m, width=700, height=500)
    clicked_coords = map_data.get("last_clicked", None)

    if clicked_coords:
        st.success(f"Koordinat dipilih: {clicked_coords['lat']:.6f}, {clicked_coords['lng']:.6f}")
    else:
        st.info("Klik lokasi pada peta untuk memilih koordinat.")


# ========================
# KOLOM 2: FORM INPUT
# ========================
with col2:
    st.markdown("### Form Prediksi Banjir")

    year = st.number_input("Tahun", min_value=2020, max_value=2100, value=2025)
    month = st.selectbox("Bulan", list(range(1, 13)), index=5)  # Juni default

    if clicked_coords:
        latitude = clicked_coords["lat"]
        longitude = clicked_coords["lng"]
    else:
        latitude = None
        longitude = None

    if st.button("Prediksi Risiko Banjir"):

        if not clicked_coords:
            st.warning("Silakan klik lokasi di peta terlebih dahulu.")
        elif not is_within_jabodetabek(latitude, longitude):
            st.error("Lokasi di luar area Jabodetabek. Silakan pilih titik dalam Jabodetabek.")
        else:
            # Panggil API
            api_url = "https://deploy-model-floodsight-production.up.railway.app/predict"
            params = {
                "year": year,
                "month": month,
                "longitude": longitude,
                "latitude": latitude
            }

            try:
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    data = response.json()

                    # Ambil data penting dari API
                    pred = data["prediction"]
                    district = data["metadata"]["district"]["NAME_2"]
                    subdistrict = data["metadata"]["district"]["NAME_3"]
                    img_year = data["metadata"]["imagery_year"]

                    status = "🟥 Risiko Banjir Tinggi" if pred == 1 else "🟩 Aman dari Banjir"

                    st.success("✅ Prediksi berhasil!")
                    st.markdown(f"""
                        **Hasil Prediksi:**  
                        {status}  

                        **Lokasi:**  
                        - Kabupaten/Kota: `{district.title()}`  
                        - Kecamatan: `{subdistrict.title()}`  
                    """)
                else:
                    st.error(f"API Error: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"Gagal menghubungi API: {e}")
