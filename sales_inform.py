import streamlit as st

# Tabela base dos planos
planos = {
    (50, 10): 286.15,
    (50, 20): 572.30,
    (50, 30): 858.45,
    (100, 10): 572.30,
    (100, 20): 1144.60,
    (100, 30): 1716.90,
    (200, 10): 1144.60,
    (200, 20): 2289.20,
    (200, 30): 3433.80,
    (500, 10): 2861.50,
    (500, 20): 5723.00,
    (500, 30): 8584.50,
}

# Categorias estratégicas
categorias = {
    "Aquisição e Expansão de Mercado": 0.20,
    "Infraestrutura e Produto": 0.25,
    "Crescimento e Estratégia de Longo Prazo": 0.15,
    "Lucro": 0.20,
    "Custo de entrega": 0.20
}

st.title("📊 Calculadora Estratégica Interna")

# Seletores de plano
usuarios = st.selectbox("Quantidade de Usuários", sorted(set([u for u, _ in planos])))
chamados = st.selectbox("Chamados por Usuário", sorted(set([c for _, c in planos])))

# Buscar custo base
custo_mensal = planos.get((usuarios, chamados), 0)
preco_mensal = custo_mensal * 7
preco_anual = preco_mensal * 12
setup_fee = 48000.00
receita_total = preco_anual + setup_fee

# Exibir valores principais
st.subheader("💰 Receita por Cliente")
st.write(f"**Custo Mensal Base:** R$ {custo_mensal:,.2f}")
st.write(f"**Preço Mensal (markup 7x):** R$ {preco_mensal:,.2f}")
st.write(f"**Preço Anual:** R$ {preco_anual:,.2f}")
st.write(f"**Setup Fee:** R$ {setup_fee:,.2f}")
st.write(f"**Receita Total (Ano 1):** R$ {receita_total:,.2f}")

# Exibir distribuição estratégica
st.subheader("📈 Distribuição Estratégica")
for categoria, pct in categorias.items():
    valor = receita_total * pct
    st.write(f"**{categoria}:** R$ {valor:,.2f}")
