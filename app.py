import streamlit as st

st.set_page_config(
    page_title="Simulador Financeiro",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título principal
st.title("📊 Simulador de Cenários Financeiros")
st.markdown("Simule resultados com base em custos, vendas e impostos.")

# Entradas organizadas em duas colunas
col1, col2 = st.columns(2)

with col1:
    receita = st.number_input("Receita Total (R$)", value=50000.0, step=1000.0, format="%.2f")
    custo = st.number_input("Custo Total (R$)", value=30000.0, step=1000.0, format="%.2f")

with col2:
    impostos = st.slider("Impostos (%)", min_value=0, max_value=50, value=15)
    crescimento = st.slider("Crescimento Projeção (%)", min_value=-50, max_value=100, value=10)

# Botão de simular
if st.button("Simular"):
    receita_liquida = receita * (1 - impostos / 100)
    lucro = receita_liquida - custo
    receita_proj = receita_liquida * (1 + crescimento / 100)
    lucro_proj = receita_proj - custo

    st.subheader("📈 Resultados")
    st.write(f"Receita Líquida: R$ {receita_liquida:,.2f}")
    st.write(f"Lucro Atual: R$ {lucro:,.2f}")
    st.write(f"Receita Projetada: R$ {receita_proj:,.2f}")
    st.write(f"Lucro Projetado: R$ {lucro_proj:,.2f}")
