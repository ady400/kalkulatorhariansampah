import streamlit as st
import plotly.express as px
import streamlit_lottie as st_lottie
import requests

# ------ SETTING HALAMAN ------
st.set_page_config(page_title="Kalkulator Sampah", layout="wide")

# ------ FUNGSI LOTTIE ------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_recycle = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_tno6cg2w.json")

# ------ BOTTOM MENU SIMULASI ------
menu = st.selectbox(
    label="Navigasi",
    options=["🏠 Beranda", "🧮 Kalkulator", "ℹ️ Tentang"],
    index=0,
    label_visibility="collapsed",
)

# ------ STYLE TAMBAHAN ------
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
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
        st_lottie.st_lottie(lottie_recycle, height=250)

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

# ------ TENTANG ------
elif menu == "ℹ️ Tentang":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dirancang untuk:
    - Mengedukasi tentang sampah harian rumah tangga
    - Menyediakan tips pengurangan limbah
    - Mendorong gaya hidup berkelanjutan

    **Dibuat oleh:** Kamu  
    **Teknologi:** Streamlit + Plotly + Lottie
    """)

# ------ BOTTOM NAV (Simulasi) ------
st.markdown("""
<div class="bottom-nav">
    🏠 Beranda | 🧮 Kalkulator | ℹ️ Tentang
</div>
""", unsafe_allow_html=True)
