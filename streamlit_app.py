import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# ------ SETTING HALAMAN ------
st.set_page_config(page_title="🧮Kalkulator Sampah", layout="wide")

# ------ FUNGSI LOTTIE ------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------ LOAD LOTTIE ANIMASI ------
lottie_recycle = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_tno6cg2w.json")
lottie_sort = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json")
lottie_truck = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_puciaact.json")
lottie_compost = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0fhlytwe.json")
lottie_landfill = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q5pk6p1k.json")
lottie_info = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t24tpvcu.json")
lottie_sidebar = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t24tpvcu.json")


# ------ MENU NAVIGASI ------
st.sidebar.title("Menu Navigasi")
 st_lottie(lottie_sidebar, speed=1, loop=True, quality="high", height=150)
menu = st.sidebar.radio(
    "Pilih Halaman",
    options=["🏠 Beranda", "🧮 Kalkulator", "🔄 Proses", "ℹ️ Tentang"]
)

# ------ STYLE TAMBAHAN ------
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f4f3;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .bottom-nav {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f4f3;
        padding: 10px 0;
        text-align: center;
        font-size: 16px;
        color: #2E7D32;
        border-top: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# ------ BERANDA ------
if menu == "🏠 Beranda":
    st.title("♻️ Kalkulator Sampah Harian")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Selamat Datang!")
        st.write("Aplikasi ini membantumu menghitung estimasi sampah rumah tangga dan memberi tips ramah lingkungan.")
    with col2:
        st_lottie(lottie_recycle, height=250)

# ------ KALKULATOR ------
elif menu == "🧮 Kalkulator":
    st.title("🧮 Hitung Sampah Harianmu")
    st.write("Masukkan jumlah orang & aktivitas harian:")

    people = st.slider("Jumlah orang di rumah", 1, 10, 3)
    activity = st.selectbox("Tingkat aktivitas harian", ["Normal", "Aktif", "Banyak belanja"])

    base_waste = 0.7
    if activity == "Aktif":
        base_waste += 0.2
    elif activity == "Banyak belanja":
        base_waste += 0.5

    total = round(people * base_waste, 2)
    organik = total * 0.6
    anorganik = total * 0.35
    b3 = total * 0.05

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Sampah", f"{total} kg")
    with col2:
        st.metric("Sampah per Orang", f"{base_waste:.2f} kg")

    fig = px.pie(
        names=["Organik", "Anorganik", "B3"],
        values=[organik, anorganik, b3],
        color_discrete_sequence=['#81C784', '#4FC3F7', '#FF8A65'],
        title="Komposisi Sampah"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Tips")
    if organik > anorganik:
        st.success("Mulai kompos dari sekarang!")
    if anorganik > 1:
        st.info("Kurangi plastik dan belanja bijak.")
    if b3 > 0.1:
        st.warning("Pisahkan limbah B3 seperti baterai!")

# ------ PROSES ------
elif menu == "🔄 Proses":
    st.title("🔄 Proses Pengelolaan Sampah")

    st.markdown("Berikut adalah tahapan umum dalam pengelolaan sampah rumah tangga:")

    with st.expander("📌 1. Pemilahan"):
        st.write("Pisahkan sampah menjadi Organik, Anorganik, dan B3 sejak di rumah.")
        st_lottie(lottie_sort, height=200)

    with st.expander("📌 2. Pengumpulan"):
        st.write("Sampah dikumpulkan berdasarkan jenis untuk memudahkan pemrosesan.")
        st_lottie(lottie_truck, height=200)

    with st.expander("📌 3. Pengangkutan"):
        st.write("Petugas kebersihan mengangkut sampah ke TPS atau pusat daur ulang.")
        st_lottie(lottie_truck, height=200)

    with st.expander("📌 4. Pemrosesan / Daur Ulang"):
        st.write("Organik → Kompos, Anorganik → Daur ulang, B3 → Penanganan khusus.")
        st_lottie(lottie_compost, height=200)

    with st.expander("📌 5. Pembuangan Akhir"):
        st.write("Sampah sisa yang tidak bisa diproses dibuang ke TPA secara aman.")
        st_lottie(lottie_landfill, height=200)

# ------ TENTANG ------
elif menu == "ℹ️ Tentang":
    st.title("ℹ️ Tentang Aplikasi")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        Aplikasi ini dirancang untuk:
        - Mengedukasi tentang sampah harian rumah tangga  
        - Menyediakan tips pengurangan limbah  
        - Mendorong gaya hidup berkelanjutan  

        **Dibuat oleh:** Nama Kamu  
        **Teknologi:** Streamlit + Plotly + Lottie  
        """)
    with col2:
        st_lottie(lottie_info, height=250)
