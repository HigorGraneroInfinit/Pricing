import streamlit as st
import pandas as pd

def calcular_itsm():
# Tabela de preços baseada no markup de 7x
    data = [
        [50, 10, 286.15],
        [50, 20, 572.30],
        [50, 30, 858.45],
        [100, 10, 572.30],
        [100, 20, 1144.60],
        [100, 30, 1716.90],
        [200, 10, 1144.60],
        [200, 20, 2289.20],
        [200, 30, 3433.80],
        [500, 10, 2861.50],
        [500, 20, 5723.00],
        [500, 30, 8584.50],
    ]

    # Criar DataFrame
    df = pd.DataFrame(data, columns=["Quantidade Usuários", "Chamados por Usuário", "Custo Mensal"])

    # Aplicar Markup de 7x
    df["Preço Mensal"] = df["Custo Mensal"] * 7

    # Calcular preço anual
    df["Preço Anual"] = df["Preço Mensal"] * 12

    # Formatar valores para Real (R$)
    df["Custo Mensal"] = df["Custo Mensal"].apply(lambda x: f"R$ {x:,.2f}")
    df["Preço Mensal"] = df["Preço Mensal"].apply(lambda x: f"R$ {x:,.2f}")
    df["Preço Anual"] = df["Preço Anual"].apply(lambda x: f"R$ {x:,.2f}")

    # Criar interface do Streamlit
    st.header("🎨 Calculadora de Preços - Chatbot ITSM")

    st.write("Selecione o número de usuários e a quantidade média de chamados que cada usuário pode abrir para calcular o custo.")

    # Opções disponíveis
    usuarios = df["Quantidade Usuários"].unique()
    chamados = df["Chamados por Usuário"].unique()

    # Seletores interativos
    qtd_usuarios = st.selectbox("📌 Escolha a quantidade de usuários:", usuarios)
    qtd_chamados = st.selectbox("📌 Escolha a média de chamados por usuário:", chamados)

    # Filtrar os valores correspondentes na tabela
    resultado = df[(df["Quantidade Usuários"] == qtd_usuarios) & (df["Chamados por Usuário"] == qtd_chamados)]

    # Exibir o preço final
    if not resultado.empty:
        st.subheader("💵 Preço Calculado")
        st.write(f"**📅 Preço Mensal:** {resultado.iloc[0]['Preço Mensal']}")
        st.write(f"**📆 Preço Anual:** {resultado.iloc[0]['Preço Anual']}")
    else:
        st.write("⚠️ Selecione valores válidos.")

    st.write("🔹 **Setup Fee fixo:** R$ 48.000,00")