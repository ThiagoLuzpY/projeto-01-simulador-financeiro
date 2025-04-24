import streamlit as st

st.set_page_config(
    page_title="Simulador Financeiro Avançado",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título
st.title("📊 Simulador de Cenários Financeiros Avançado")
st.markdown("Simule resultados com base em receitas, custos e **impostos discriminados** por categoria.")

# Entradas básicas
col1, col2 = st.columns(2)

with col1:
    receita = st.number_input("Receita Bruta (R$)", value=50000.0, step=1000.0, format="%.2f")
    custo = st.number_input("Custo Total (R$)", value=30000.0, step=1000.0, format="%.2f")

with col2:
    crescimento = st.slider("Crescimento Projeção (%)", min_value=-50, max_value=100, value=10)

# Impostos individualizados
st.markdown("### 🧾 Impostos (% sobre Receita Bruta)")

col_icms, col_st = st.columns(2)
with col_icms:
    icms = st.number_input("ICMS (%)", min_value=0.0, max_value=30.0, value=18.0, step=0.5)
    pis = st.number_input("PIS (%)", min_value=0.0, max_value=10.0, value=1.65, step=0.05)
    cofins = st.number_input("COFINS (%)", min_value=0.0, max_value=10.0, value=7.6, step=0.1)

with col_st:
    icms_st = st.number_input("ICMS-ST (ex: Ceará) (%)", min_value=0.0, max_value=20.0, value=0.0, step=0.5)
    ipi = st.number_input("IPI (%)", min_value=0.0, max_value=20.0, value=0.0, step=0.5)
    fundo_rj = st.number_input("Fundo Pobreza RJ (%)", min_value=0.0, max_value=5.0, value=2.0, step=0.5)

# Cálculos
if st.button("Simular"):
    total_impostos = sum([icms, pis, cofins, ipi, icms_st, fundo_rj])
    valor_impostos = receita * total_impostos / 100
    receita_liquida = receita - valor_impostos
    lucro = receita_liquida - custo
    receita_proj = receita_liquida * (1 + crescimento / 100)
    lucro_proj = receita_proj - custo

    st.subheader("📈 Resultados")
    st.write(f"Total de Impostos (%): **{total_impostos:.2f}%**")
    st.write(f"Valor Total de Impostos: R$ {valor_impostos:,.2f}")
    st.write(f"Receita Líquida: R$ {receita_liquida:,.2f}")
    st.write(f"Lucro Atual: R$ {lucro:,.2f}")
    st.write(f"Receita Projetada: R$ {receita_proj:,.2f}")
    st.write(f"Lucro Projetado: R$ {lucro_proj:,.2f}")
