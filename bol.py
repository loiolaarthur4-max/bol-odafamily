import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Bolão Oficial 2026", layout="wide")

# Estilo profissional
st.markdown("""
    <style>
    .card { background: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #ddd; }
    .stApp { background-color: #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

# Dicionário de jogos
jogos_oficiais = {
    "1": {"time_casa": "Canadá", "time_fora": "Marrocos", "data": "04/07"},
    "3": {"time_casa": "Brasil", "time_fora": "Noruega", "data": "05/07"}
}

# --- LÓGICA DE CLASSIFICAÇÃO ---
def carregar_pontuacao():
    if not os.path.isfile("palpites.csv"):
        return pd.DataFrame({"Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"], "Pontos": [0, 0, 0]})
    # Aqui entraria a lógica de ler o CSV e somar pontos baseada nos resultados oficiais
    return pd.DataFrame({"Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"], "Pontos": [0, 0, 0]})

# --- INTERFACE ---
col_tabela, col_palpite = st.columns([1, 2])

with col_tabela:
    st.subheader("📊 Tabela de Grupos")
    df = carregar_pontuacao()
    st.table(df.set_index("Grupo"))

with col_palpite:
    st.subheader("⚽ Registrar Palpite")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        with st.form("form_palpite"):
            # (Seu código de formulário permanece o mesmo...)
            grupo = st.selectbox("Seu Grupo", ["Grupo 1", "Grupo 2", "Grupo 3"])
            nome = st.selectbox("Seu Nome", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Tio Israel", "Tia Socorro", "Constantino", "Juliane", "Tino"])
            senha = st.text_input("Senha", type="password")
            
            c1, c2 = st.columns(2)
            gols_casa = c1.number_input("Gols Casa", min_value=0)
            gols_fora = c2.number_input("Gols Fora", min_value=0)
            
            if st.form_submit_button("Confirmar Palpite"):
                if senha == "1234":
                    st.success("Palpite registrado!")
                else:
                    st.error("Senha incorreta!")
        st.markdown('</div>', unsafe_allow_html=True)
