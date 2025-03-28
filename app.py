import streamlit as st

def calcular_precificacao():
    st.title("💰 Calculadora de Preço - Novo Produto")
    
    # Tabela de preços de acordo com o número de usuários e chamados
    precos = {
        ("0-10", 10): {"custo_mensal": 57.08, "capacidade": 100, "chamados_usuario": 10},
        ("0-10", 20): {"custo_mensal": 114.16, "capacidade": 200, "chamados_usuario": 20},
        ("0-10", 30): {"custo_mensal": 171.24, "capacidade": 300, "chamados_usuario": 30},
        ("11-20", 10): {"custo_mensal": 570.80, "capacidade": 200, "chamados_usuario": 10},
        ("11-20", 20): {"custo_mensal": 228.32, "capacidade": 400, "chamados_usuario": 20},
        ("11-20", 30): {"custo_mensal": 342.48, "capacidade": 600, "chamados_usuario": 30},
        ("21-30", 10): {"custo_mensal": 171.24, "capacidade": 300, "chamados_usuario": 10},
        ("21-30", 20): {"custo_mensal": 342.48, "capacidade": 600, "chamados_usuario": 20},
        ("21-30", 30): {"custo_mensal": 513.72, "capacidade": 900, "chamados_usuario": 30},
        ("31-40", 10): {"custo_mensal": 228.32, "capacidade": 400, "chamados_usuario": 10},
        ("31-40", 20): {"custo_mensal": 456.64, "capacidade": 800, "chamados_usuario": 20},
        ("31-40", 30): {"custo_mensal": 684.96, "capacidade": 1200, "chamados_usuario": 30},
    }

    # Seleção de faixa de usuários e média de chamados por usuário
    usuarios = st.selectbox("Escolha a faixa de usuários:", ["0-10", "11-20", "21-30", "31-40"])
    chamados = st.selectbox("Escolha a quantidade de chamados por usuário:", [10, 20, 30])

    # Obter os valores da tabela de preços
    chave = (usuarios, chamados)
    if chave in precos:
        dados = precos[chave]
        custo_mensal = dados["custo_mensal"]
        capacidade = dados["capacidade"]
        chamados_usuario = dados["chamados_usuario"]

        # Cálculo do setup fee baseado em horas e valor
        taxa_hora = 180.00  # R$ 180 por hora (taxa atual do consultor)
        horas_implementacao = 80  # horas estimadas para implementação
        markup = 2.0  # Markup para cobrir outros custos e gerar margem (exemplo: 2x)

        # Cálculo do valor do Setup Fee
        custo_implementacao = horas_implementacao * 100  # custo base
        setup_fee = 24000  # aplicar markup

        # Cálculo do preço de venda com markup 7x
        preco_venda_mensal = custo_mensal * 10  # Markup 7x
        preco_venda_anual = preco_venda_mensal * 12  # Anualidade

        # **Banco de horas de 40h por mês** para melhorias e integrações
        horas_mensal_banco = 40  # Pacote de horas para melhorias
        custo_banco_horas = horas_mensal_banco * 100  # custo do banco de horas
        custo_banco_horas_2 = horas_mensal_banco * 180

        # Cálculos de Margem
        margem_mensal = ((preco_venda_mensal - custo_mensal) / preco_venda_mensal) * 100
        margem_anual = ((preco_venda_anual - custo_mensal * 12) / (preco_venda_anual)) * 100

        # Exibir os valores calculados
        st.subheader("1 - Capacidade da Ferramenta")
        st.write(f"**Capacidade de Chamados:** {capacidade} chamados")
        st.write(f"**Média de Chamados por Usuário:** {chamados_usuario} chamados")

        st.subheader("2 - Custo da Ferramenta - Prime Control")
        st.write(f"**Custo Mensal:** R$ {custo_mensal:,.2f}")
        st.write(f"**Custo de Implementação (80h de Setup):** R$ {custo_implementacao:,.2f}")
        st.write(f"**Custo de Sustentação (40h/mês):** R$ {custo_banco_horas:,.2f}")

        st.subheader("3 - Preço da Ferramenta - Cliente")
        st.write(f"**Setup Fee - Ferramenta:** R$ {setup_fee:,.2f}")
        st.write(f"**Preço de Venda Mensal (Markup 10x) - Ferramenta:** R$ {preco_venda_mensal:,.2f}")
        st.write(f"**Preço de Venda Anual - Ferramenta:** R$ {preco_venda_anual:,.2f}")
        st.write(f"**Banco de Horas (40h/mês) para Melhorias e Integrações: - Suporte** R$ {custo_banco_horas_2:,.2f}")

        valor_total_venda_ano = ( setup_fee + preco_venda_anual + (custo_banco_horas_2 * 12) )
        valor_total_venda_mes = custo_banco_horas_2 + preco_venda_mensal

        st.subheader("4 - Valor Final - Cliente")
        st.write(f"**Valor Total Final - Mês:** R$ {valor_total_venda_mes:,.2f}")
        st.write(f"**Valor Total Final - Ano:** R$ {valor_total_venda_ano:,.2f}")

        # Exibição gráfica de Custo vs Venda (Opcional)
        # fig, ax = plt.subplots()
        #x.bar(["Custo Mensal", "Venda Mensal"], [custo_mensal, preco_venda_mensal], color=["blue", "green"])
        #ax.set_title("Custo vs Venda Mensal")
        #ax.set_ylabel("Valor (R$)")
        #st.pyplot(fig)

# Rodar a função no Streamlit
if __name__ == "__main__":
    calcular_precificacao()
