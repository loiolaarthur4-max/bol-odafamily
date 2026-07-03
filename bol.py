import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bolão da Família 2026", layout="wide")

st.title("🏆 Bolão da Copa do Mundo 2026")

# Exemplo de dados (você pode carregar isso de um arquivo CSV depois)
dados = {
    'Grupo': ['Grupo 1', 'Grupo 2', 'Grupo 3'],
    'Participantes': ['Davi, Arthur, Victor, Kharla', 'Renan, Fabio, Israel, Socorro', 'Constantino, Juliane, Tino'],
    'Pontos': [0, 0, 0]
}

df = pd.DataFrame(dados)

st.subheader("Classificação Atual")
st.table(df)

st.divider()

st.subheader("Registrar Palpite")
with st.form("meu_palpite"):
    nome = st.selectbox("Quem está palpitando?", ["Davi", "Arthur", "Victor", "Kharla", "Renan", "Fabio", "Israel", "Socorro", "Constantino", "Juliane", "Tino"])
    jogo = st.text_input("Jogo (Ex: Brasil x Japão)")
    placar = st.text_input("Placar (Ex: 2-1)")
    submit = st.form_submit_button("Enviar Palpite")

    if submit:
        # AQUI VOCÊ PODE ADICIONAR A LÓGICA DE TEMPO
        # Exemplo: Se (hora_atual - hora_jogo) > 30 min, não aceita.
        st.success(f"Palpite de {nome} registrado para {jogo}!")
