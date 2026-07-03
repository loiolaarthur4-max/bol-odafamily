import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="Bolão Copa 2026", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stApp { border: 1px solid #dee2e6; border-radius: 10px; padding: 20px; }
    .card { background: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    h1 { color: #1e3a8a; text-align: center; font-family: sans-serif; }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1>⚽ World Cup 2026 Bolão</h1>", unsafe_allow_html=True)

# --- TABELA DE CLASSIFICAÇÃO (SIMULADA) ---
st.subheader("📊 Classificação")
df = pd.DataFrame({
    "Pos": ["🥇 1º", "🥈 2º", "🥉 3º"],
    "Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"],
    "Pontos": [0, 0, 0]
})
st.table(df.set_index("Pos"))

# --- ÁREA DE PALPITES ---
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Registrar Palpite")
    
    with st.form("form_palpite"):
        col1, col2 = st.columns(2)
        grupo = col1.selectbox("Seu Grupo", ["Grupo 1", "Grupo 2", "Grupo 3"])
        nome = col2.selectbox("Seu Nome", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Israel", "Socorro", "Constantino", "Juliane", "Tino"])
        
        senha = st.text_input("Senha de Segurança", type="password")
        
        col_g1, col_g2 = st.columns(2)
        gols_casa = col_g1.number_input("Brasil", min_value=0, step=1)
        gols_fora = col_g2.number_input("França", min_value=0, step=1)
        
        btn = st.form_submit_button("Confirmar Palpite")
        
        if btn:
            if senha == "1234": # Configure sua senha secreta aqui
                st.success(f"Palpite de {nome} registrado com sucesso!")
            else:
                st.error("Senha incorreta!")
    st.markdown('</div>', unsafe_allow_html=True)
