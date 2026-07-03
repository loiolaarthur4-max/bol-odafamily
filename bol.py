import streamlit as st
import pandas as pd

# Configuração Visual
st.set_page_config(page_title="Bolão Oficial 2026", layout="centered")

st.markdown("""
    <style>
    .card { background: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #ddd; margin-bottom: 20px; }
    .stApp { background-color: #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

# Dicionário de Jogos Oficiais das Oitavas de Final (2026)
jogos_oficiais = {
    "1": {"time_casa": "Canadá", "time_fora": "Marrocos", "data": "04/07"},
    "2": {"time_casa": "Paraguai", "time_fora": "França", "data": "04/07"},
    "3": {"time_casa": "Brasil", "time_fora": "Noruega", "data": "05/07"},
    "4": {"time_casa": "México", "time_fora": "Inglaterra", "data": "05/07"}
}

st.title("⚽ Bolão Copa do Mundo 2026")

# Seleção de Jogo
st.subheader("🗓️ Próximas Partidas")
jogo_id = st.selectbox("Escolha o jogo para palpitar:", 
                       options=list(jogos_oficiais.keys()), 
                       format_func=lambda x: f"{jogos_oficiais[x]['time_casa']} vs {jogos_oficiais[x]['time_fora']} ({jogos_oficiais[x]['data']})")

jogo_selecionado = jogos_oficiais[jogo_id]

# Formulário de Palpite
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"Palpite: {jogo_selecionado['time_casa']} x {jogo_selecionado['time_fora']}")
    
    with st.form("palpite_form"):
        grupo = st.selectbox("Seu Grupo", ["Grupo 1", "Grupo 2", "Grupo 3"])
        nome = st.selectbox("Seu Nome", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Tio Israel", "Tia Socorro", "Constantino", "Juliane", "Tino"])
        
        c1, c2 = st.columns(2)
        gols_casa = c1.number_input(f"{jogo_selecionado['time_casa']}", min_value=0, max_depth=10)
        gols_fora = c2.number_input(f"{jogo_selecionado['time_fora']}", min_value=0, max_depth=10)
        
        btn = st.form_submit_button("Registrar Palpite")
        
        if btn:
            # Aqui você registrará no banco de dados (ex: salvar em arquivo ou banco SQL)
            st.success(f"Palpite de {nome} para {jogo_selecionado['time_casa']} {gols_casa}x{gols_fora} {jogo_selecionado['time_fora']} registrado!")
    st.markdown('</div>', unsafe_allow_html=True)
