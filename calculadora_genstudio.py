import streamlit as st

def calcular_genstudio():
    st.header("🎨 GenStudio - Calculadora de Preços")

    # Faixas de precificação
    precos = {
        "de 0 até 20": {"unit": 185, "mensal": 3700, "anual": 44400},
        "de 21 até 50": {"unit": 160, "mensal": 8000, "anual": 96000},
        "de 51 até 100": {"unit": 145, "mensal": 14500, "anual": 174000},
    }

    # Selectbox com as faixas
    faixa_escolhida = st.selectbox("Selecione a faixa de licenças desejada:", list(precos.keys()))

    # Dados do plano
    plano = precos[faixa_escolhida]

    # Exibição dos valores
    st.subheader("💰 Resultado")
    st.write(f"**Faixa selecionada:** {faixa_escolhida}")
    st.write(f"**Valor unitário:** R$ {plano['unit']:,.2f}")
    st.write(f"**Valor mensal:** R$ {plano['mensal']:,.2f}")
    st.write(f"**Valor anual:** R$ {plano['anual']:,.2f}")