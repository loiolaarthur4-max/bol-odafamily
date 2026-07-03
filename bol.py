import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bolão Oficial 2026", layout="wide")

# --- DADOS ---
jogos_oficiais = {
    "1": "Canadá x Marrocos (04/07)",
    "2": "Paraguai x França (04/07)",
    "3": "Brasil x Noruega (05/07)",
    "4": "México x Inglaterra (05/07)"
}

grupos = {
    "Grupo 1": ["Davi", "Arthur", "Victor", "Kharla"],
    "Grupo 2": ["Renan", "Fabio", "Tio Israel", "Tia Socorro"],
    "Grupo 3": ["Constantino", "Juliane", "Tino"]
}

# --- FUNÇÃO DE RANKING ---
def mostrar_ranking():
    # Aqui você substituirá pelos dados reais do seu CSV de palpites
    data = {
        "Nome": ["Tino", "Davi", "Renan", "Kharla", "Fabio"],
        "Grupo": ["Grupo 3", "Grupo 1", "Grupo 2", "Grupo 1", "Grupo 2"],
        "Pontos": [85, 80, 75, 70, 65] # Exemplo de pontos
    }
    df = pd.DataFrame(data).sort_values(by="Pontos", ascending=False)
    df.index = range(1, len(df) + 1)
    return df

# --- INTERFACE ---
col_tabela, col_palpite = st.columns([1.5, 1])

with col_tabela:
    st.subheader("🏆 Ranking Geral (Indivídual)")
    st.dataframe(mostrar_ranking(), use_container_width=True)

with col_palpite:
    st.subheader("📝 Palpites")
    with st.form("palpite_form"):
        # Filtro dinâmico: Ao escolher o grupo, muda os nomes
        grupo_selecionado = st.selectbox("Escolha seu Grupo", list(grupos.keys()))
        participante = st.selectbox("Escolha seu Nome", grupos[grupo_selecionado])
        
        jogo = st.selectbox("Escolha o Jogo", list(jogos_oficiais.values()))
        
        c1, c2 = st.columns(2)
        casa = c1.number_input("Gols Casa", min_value=0)
        fora = c2.number_input("Gols Fora", min_value=0)
        
        senha = st.text_input("Senha", type="password")
        
        if st.form_submit_button("Enviar"):
            # Lógica de salvar...
            st.success(f"Palpite de {participante} ({grupo_selecionado}) registrado!")

# --- TABELA DE GRUPOS (Médias) ---
st.divider()
st.subheader("📊 Ranking por Grupo")
# Lógica que soma os pontos de todos do grupo e divide pela quantidade de membros
df_grupos = pd.DataFrame({
    "Grupo": ["Grupo 1", "Grupo 2", "Grupo 3"],
    "Pontos Médios": [75, 70, 85]
}).sort_values(by="Pontos Médios", ascending=False)
st.table(df_grupos.set_index("Grupo"))
