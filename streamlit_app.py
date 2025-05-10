import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Kalkulator Sampah Harian", layout="centered")

# ---------- UI HEADER ----------
st.markdown("""
    <style>
        .title {
            font-size: 30px;
            font-weight: bold;
            color: #2E7D32;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtext {
            font-size: 16px;
            color: gray;
            text-align: center;
            margin-bottom: 30px;
        }
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #f0f4f3;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            text-align: center;
            font-size: 18px;
        }
    </style>
    <div class="title">♻️ Kalkulator Sampah Harian</div>
    <div class="subtext">Hitung estimasi sampah rumahmu dan dapatkan tips ramah lingkungan</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
people = st.slider("Berapa orang di rumah?", 1, 10, 3)
activity = st.selectbox("Tingkat aktivitas harian?", ["Normal", "Aktif", "Banyak belanja"])

base_waste = 0.7
if activity == "Aktif":
    base_waste += 0.2
elif activity == "Banyak belanja":
    base_waste += 0.5

total_waste = round(people * base_waste, 2)
organik = total_waste * 0.6
anorganik = total_waste * 0.35
b3 = total_waste * 0.05

# ---------- INFO CARDS ----------
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='card'>Total Sampah:<br><b>{total_waste} kg</b></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='card'>Sampah per Orang:<br><b>{base_waste:.2f} kg</b></div>", unsafe_allow_html=True)

# ---------- GRAFIK PIE ----------
fig = px.pie(
    names=["Organik", "Anorganik", "B3"],
    values=[organik, anorganik, b3],
    color_discrete_sequence=['#81C784', '#4FC3F7', '#FF8A65'],
    title="Komposisi Sampah"
)
fig.update_traces(textinfo='label+percent')
st.plotly_chart(fig, use_container_width=True)

# ---------- TIPS ----------
st.markdown("### Tips Pengurangan Sampah")
with st.container():
    if organik > anorganik:
        st.success("Komposkan sampah organik untuk pupuk alami!")
    if anorganik > 1:
        st.info("Kurangi plastik sekali pakai. Gunakan botol & tas reusable.")
    if b3 > 0.1:
        st.warning("Pisahkan limbah B3! Jangan dibuang bersama sampah biasa.")

st.markdown("---")
st.caption("Dibuat dengan Streamlit | Edukasi Lingkungan")
