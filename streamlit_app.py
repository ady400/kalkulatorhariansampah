import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Kalkulator Sampah Harian", layout="wide")

# ---------- MENU NAVIGASI ----------
menu = st.sidebar.radio("Menu", ["Beranda", "Kalkulator", "Tentang Aplikasi"])

# ---------- BERANDA ----------
if menu == "Beranda":
    st.title("♻️ Selamat Datang di Kalkulator Sampah Harian")
    st.markdown("""
        Aplikasi ini membantu kamu menghitung estimasi sampah rumah tangga dan memberi tips pengurangannya.
        
        **Gunakan menu di kiri untuk mulai kalkulasi.**
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/849/849379.png", width=200)

# ---------- KALKULATOR ----------
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Sampah Harian")

    people = st.slider("Jumlah orang di rumah", 1, 10, 3)
    activity = st.selectbox("Tingkat aktivitas harian", ["Normal", "Aktif", "Banyak belanja"])

    base_waste = 0.7
    if activity == "Aktif":
        base_waste += 0.2
    elif activity == "Banyak belanja":
        base_waste += 0.5

    total_waste = round(people * base_waste, 2)
    organik = total_waste * 0.6
    anorganik = total_waste * 0.35
    b3 = total_waste * 0.05

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Sampah / Hari", f"{total_waste} kg")
    with col2:
        st.metric("Per Orang", f"{base_waste:.2f} kg")

    fig = px.pie(
        names=["Organik", "Anorganik", "B3"],
        values=[organik, anorganik, b3],
        color_discrete_sequence=['#81C784', '#4FC3F7', '#FF8A65'],
        title="Komposisi Sampah"
    )
    fig.update_traces(textinfo='label+percent')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Tips Pengurangan Sampah")
    if organik > anorganik:
        st.success("Mulai kompos sampah organik!")
    if anorganik > 1:
        st.info("Kurangi sampah plastik dengan tas belanja & botol minum.")
    if b3 > 0.1:
        st.warning("Pisahkan limbah B3 seperti baterai & obat.")

# ---------- TENTANG ----------
elif menu == "Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dirancang untuk:
    
    - Membantu masyarakat menghitung sampah harian rumah tangga.
    - Menyediakan tips edukatif untuk mengurangi limbah.
    - Mendorong gaya hidup berkelanjutan.

    **Dibuat dengan:** Python & Streamlit  
    **Versi:** 1.0  
    **Pengembang:** [Nama kamu atau tim]  
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/3616/3616591.png", width=150)

st.markdown("---")
st.caption("© 2025 - Edukasi Sampah & Lingkungan | Dibuat dengan Streamlit")
