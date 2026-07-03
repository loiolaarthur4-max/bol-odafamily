import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Bolão Oficial 2026", layout="wide")

# 1. Configuração de Senhas (Individual)
# Dica: Você pode mudar essas senhas depois
senhas_usuarios = {
    "Davi": "1234", "Arthur": "2222", "Victor": "3333", "Kharla": "4444",
    "Renan": "5555", "Fabio": "6666", "Tio Israel": "7777", "Tia Socorro": "8888",
    "Constantino": "9999", "Juliane": "1010", "Tino": "1111"
}

# 2. Dados dos Grupos
grupos = {
    "Grupo 1": ["Davi", "Arthur", "Victor", "Kharla"],
    "Grupo 2": ["Renan", "Fabio", "Tio Israel", "Tia Socorro"],
    "Grupo 3": ["Constantino", "Juliane", "Tino"]
}

# 3. Lógica de Tabela
def mostrar_tabela():
    data = {"Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"], "Pontos": [0, 0, 0]}
    return pd.DataFrame(data)

# Layout da Interface
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Tabela de Grupos")
    st.table(mostrar_tabela().set_index("Grupo"))

with col2:
    st.subheader("📝 Registrar Palpite")
    with st.form("form_palpite"):
        # Seleção encadeada
        grupo_escolhido = st.selectbox("Selecione seu Grupo", list(grupos.keys()))
        nome = st.selectbox("Seu Nome", grupos[grupo_escolhido])
        senha = st.text_input("Digite sua senha pessoal", type="password")
        
        st.write("---")
        c1, c2 = st.columns(2)
        gols_casa = c1.number_input("Gols Casa", min_value=0, max_value=10)
        gols_fora = c2.number_input("Gols Fora", min_value=0, max_value=10)
        
        btn = st.form_submit_button("Confirmar Palpite")
        
        if btn:
            # Validação da Senha
            if senha == senhas_usuarios.get(nome):
                # Salvar em CSV (Persistência)
                df_palpite = pd.DataFrame([[nome, grupo_escolhido, gols_casa, gols_fora]], 
                                          columns=["Nome", "Grupo", "Gols_Casa", "Gols_Fora"])
                
                caminho = "palpites.csv"
                if not os.path.isfile(caminho):
                    df_palpite.to_csv(caminho, index=False)
                else:
                    df_palpite.to_csv(caminho, mode='a', header=False, index=False)
                
                st.success(f"Palpite de {nome} salvo com sucesso!")
            else:
                st.error("Senha incorreta para este usuário!")
