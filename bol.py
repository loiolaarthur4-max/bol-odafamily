import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(page_title="Bolão Oficial 2026", layout="centered")

st.markdown("""
    <style>
    .card { background: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #ddd; margin-bottom: 20px; }
    .stApp { background-color: #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

# Dicionário de Jogos
jogos_oficiais = {
    "1": {"time_casa": "Canadá", "time_fora": "Marrocos", "data": "04/07"},
    "2": {"time_casa": "Paraguai", "time_fora": "França", "data": "04/07"},
    "3": {"time_casa": "Brasil", "time_fora": "Noruega", "data": "05/07"},
    "4": {"time_casa": "México", "time_fora": "Inglaterra", "data": "05/07"}
}

# Função para salvar palpites
def salvar_palpite(nome, grupo, jogo, g1, g2):
    caminho = "palpites.csv"
    dados = pd.DataFrame([[nome, grupo, jogo, g1, g2]], 
                         columns=["Nome", "Grupo", "Jogo", "Gols_Casa", "Gols_Fora"])
    if not os.path.isfile(caminho):
        dados.to_csv(caminho, index=False)
    else:
        dados.to_csv(caminho, mode='a', header=False, index=False)

st.title("⚽ Bolão Copa do Mundo 2026")

jogo_id = st.selectbox("Escolha o jogo:", options=list(jogos_oficiais.keys()), 
                       format_func=lambda x: f"{jogos_oficiais[x]['time_casa']} vs {jogos_oficiais[x]['time_fora']} ({jogos_oficiais[x]['data']})")

jogo_sel = jogos_oficiais[jogo_id]

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    with st.form("form_palpite"):
        grupo = st.selectbox("Seu Grupo", ["Grupo 1", "Grupo 2", "Grupo 3"])
        nome = st.selectbox("Seu Nome", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Tio Israel", "Tia Socorro", "Constantino", "Juliane", "Tino"])
        senha = st.text_input("Senha de Segurança", type="password")
        
        c1, c2 = st.columns(2)
        gols_casa = c1.number_input(f"{jogo_sel['time_casa']}", min_value=0, max_value=10)
        gols_fora = c2.number_input(f"{jogo_sel['time_fora']}", min_value=0, max_value=10)
        
        btn = st.form_submit_button("Registrar Palpite")
        
        if btn:
            # Senha mestra (ou crie uma lógica individual aqui)
            if senha == "1234":
                salvar_palpite(nome, grupo, f"{jogo_sel['time_casa']}x{jogo_sel['time_fora']}", gols_casa, gols_fora)
                st.success(f"Palpite registrado para {nome}!")
            else:
                st.error("Senha incorreta!")
    st.markdown('</div>', unsafe_allow_html=True)
