import streamlit as st
import pandas as pd

# Configuração de Estilo Profissional
st.set_page_config(page_title="Bolão Copa 2026", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #004a99; color: white; }
    h1 { color: #004a99; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 FIFA World Cup 2026 - Bolão Oficial")

# Tabela Profissional
st.subheader("📊 Classificação")
data = {
    "Pos": ["1º", "2º", "3º"],
    "Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"],
    "Pontos": [0, 0, 0]
}
df = pd.DataFrame(data)

# Estilizando a tabela para ficar bonita
st.table(df.style.set_properties(**{'text-align': 'center'}))

# Área de Palpite (Card)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📝 Registrar Palpite")
with st.form("palpite_profissional"):
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Selecione seu Grupo", ["Grupo 1", "Grupo 2", "Grupo 3"])
    with col2:
        participante = st.selectbox("Selecione seu Nome", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Israel", "Socorro", "Constantino", "Juliane", "Tino"])
    
    st.text_input("Senha de Acesso", type="password")
    
    # Campo de Placar com design melhor
    c1, c2 = st.columns(2)
    gol1 = c1.number_input("Brasil", min_value=0, step=1)
    gol2 = c2.number_input("França", min_value=0, step=1)
    
    submitted = st.form_submit_button("CONFIRMAR PALPITE")
    if submitted:
        st.balloons()
        st.success("Palpite registrado com sucesso no sistema!")
st.markdown('</div>', unsafe_allow_html=True)
