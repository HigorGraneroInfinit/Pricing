import streamlit as st

def calcular_whats_teams():
    st.header("💬 ChatSync WhatsApp/Teams - Preço Fixo")

    setup_fee = 7500
    mensalidade = 10000
    anual = mensalidade * 12

    st.subheader("💰 Valores")
    st.write(f"**Setup Fee:** R$ {setup_fee:,.2f}")
    st.write(f"**Mensalidade:** R$ {mensalidade:,.2f}")
    st.write(f"**Anuidade:** R$ {anual:,.2f}")