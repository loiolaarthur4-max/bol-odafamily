import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Bolão Família 2026", layout="wide")

# Dados dos Grupos
participantes = {
    "Grupo 1": ["Davi", "Arthur", "Victor", "Kharla"],
    "Grupo 2": ["Renan", "Fabio", "Tio Israel", "Tia Socorro"],
    "Grupo 3": ["Constantino", "Juliane", "Tino"]
}

# Simulação de Jogo (O oficial da Copa)
# Em um cenário real, você buscaria isso de uma API de futebol
jogo_exemplo = {"time_casa": "Brasil", "time_fora": "França", "horario": datetime(2026, 7, 10, 16, 0)}

st.title("⚽ Bolão da Copa do Mundo 2026")

# 1. Tabela de Classificação
st.subheader("📊 Classificação dos Grupos")
# Aqui você criaria um DF com a pontuação real
df = pd.DataFrame({
    "Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"],
    "Pontos": [0, 0, 0]
})
st.table(df)

# 2. Sistema de Palpites (Seguro)
st.subheader(f"Palpite para: {jogo_exemplo['time_casa']} x {jogo_exemplo['time_fora']}")

with st.form("palpite_form"):
    # Para evitar que mintam o nome, selecione o grupo e depois o nome
    grupo_escolhido = st.selectbox("Escolha seu Grupo", list(participantes.keys()))
    nome = st.selectbox("Quem é você?", participantes[grupo_escolhido])
    
    # Campo para senha/chave de segurança (isso evita que um palpite pelo outro)
    senha = st.text_input("Digite sua senha de acesso", type="password")
    
    col1, col2 = st.columns(2)
    gol_casa = col1.number_input(f"Gols {jogo_exemplo['time_casa']}", min_value=0)
    gol_fora = col2.number_input(f"Gols {jogo_exemplo['time_fora']}", min_value=0)
    
    submit = st.form_submit_button("Confirmar Palpite")

    if submit:
        # Lógica de tempo (Regra dos 30 minutos)
        agora = datetime.now()
        limite = jogo_exemplo['horario'] - timedelta(minutes=30)
        
        if agora > limite:
            st.error("❌ Tempo esgotado! Você só pode palpitar até 30 minutos antes do jogo.")
        elif senha != "1234": # Crie uma senha única para cada um ou uma geral
            st.error("❌ Senha incorreta! Você não pode palpitar por outra pessoa.")
        else:
            # Aqui você salvaria o palpite no seu banco de dados
            st.success(f"Palpite de {nome} registrado com sucesso: {gol_casa} x {gol_fora}!")
