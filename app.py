import streamlit as st
import pandas as pd

# Funções separadas para cada produto
from calculadora_itsm import calcular_itsm
from calculadora_genstudio import calcular_genstudio  # <- Essa função acima
from calculadora_chatsync import calcular_whats_teams

st.title("💼 Calculadora de Produtos")

produto = st.selectbox("Selecione o produto:", ["ChatSync ITSM", "GenStudio", "ChatSync WhatsApp/Teams"])

if produto == "ChatSync ITSM":
    calcular_itsm()
elif produto == "GenStudio":
    calcular_genstudio()
elif produto == "ChatSync WhatsApp/Teams":
    calcular_whats_teams()