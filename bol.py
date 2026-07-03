import streamlit as st
import pandas as pd

# Função para criar um "Card" de jogo profissional
def render_match_card(jogo):
    with st.container():
        col1, col2, col3 = st.columns([2, 1, 2])
        col1.subheader(jogo['time_casa'])
        col2.markdown("### VS")
        col3.subheader(jogo['time_fora'])
        
        # Inputs alinhados
        p1, p2 = st.columns(2)
        palpite1 = p1.number_input(f"Gols {jogo['time_casa']}", key=f"c_{jogo['id']}")
        palpite2 = p2.number_input(f"Gols {jogo['time_fora']}", key=f"f_{jogo['id']}")
        
        if st.button("Registrar Palpite", key=f"btn_{jogo['id']}"):
            # Lógica de gravação aqui
            st.toast("Palpite enviado com sucesso!", icon="⚽")
