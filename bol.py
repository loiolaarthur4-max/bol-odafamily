import streamlit as st
import pandas as pd

# Design "Dark & Clean"
st.set_page_config(page_title="World Cup 2026 Pro", layout="wide")

st.markdown("""
    <style>
    /* Fundo degradê */
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    
    /* Cards estilo vidro */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Títulos estilizados */
    h1, h2, h3 { color: #00d2ff; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
    
    /* Botões */
    div.stButton > button { background: #00d2ff; color: #000; font-weight: bold; width: 100%; border-radius: 50px; border: none; }
    </style>
""", unsafe_allow_html=True)

# Estrutura de dados
grupos = {
    "Grupo 1": ["Davi", "Arthur", "Victor", "Kharla"],
    "Grupo 2": ["Renan", "Fabio", "Tio Israel", "Tia Socorro"],
    "Grupo 3": ["Constantino", "Juliane", "Tino"]
}

# --- LAYOUT PRINCIPAL ---
st.title("🏆 FIFA WORLD CUP 2026")
st.subheader("Painel de Performance e Palpites")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📊 Ranking Geral")
    # Tabela estilizada
    df = pd.DataFrame({"Pos": ["1º", "2º", "3º"], "Nome": ["Tino", "Davi", "Renan"], "Pts": [95, 88, 82]})
    st.table(df.set_index("Pos"))
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("⚽ Novo Palpite")
    with st.form("palpite_pro"):
        g = st.selectbox("Grupo", list(grupos.keys()))
        n = st.selectbox("Participante", grupos[g])
        j = st.selectbox("Jogo", ["Brasil x Noruega", "México x Inglaterra"])
        
        c1, c2 = st.columns(2)
        c1.number_input("Gols Casa", 0, 10)
        c2.number_input("Gols Fora", 0, 10)
        
        st.text_input("Senha de Acesso", type="password")
        st.form_submit_button("REGISTRAR PALPITE")
    st.markdown('</div>', unsafe_allow_html=True)
