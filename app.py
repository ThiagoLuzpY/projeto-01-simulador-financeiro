import streamlit as st
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Simulador Financeiro Avançado",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Título e instrução
st.markdown("<h1 style='font-size: 32px;'>📊 Simulador de Cenários Financeiros Avançado</h1>", unsafe_allow_html=True)
st.markdown("Simule resultados com base em receitas, custos e <b>impostos discriminados</b> por categoria.", unsafe_allow_html=True)

# Layout com duas colunas: esquerda (input), direita (output)
col_input, col_output = st.columns([1.2, 1.8])

# ========================
# SEÇÃO DE ENTRADA DE DADOS
# ========================
with col_input:
    st.markdown("### 🧮 Entradas")

    receita = st.number_input("Receita Bruta (R$)", value=50000.0, step=1000.0, format="%.2f", key="receita")
    custo = st.number_input("Custo Total (R$)", value=30000.0, step=1000.0, format="%.2f", key="custo")
    crescimento = st.slider("Crescimento Projeção (%)", min_value=-50, max_value=100, value=10)

    st.markdown("### 🧾 Impostos (% sobre Receita Bruta)")

    icms = st.number_input("ICMS (%)", min_value=0.0, max_value=30.0, value=18.0, step=0.5, format="%.2f")
    pis = st.number_input("PIS (%)", min_value=0.0, max_value=10.0, value=1.65, step=0.05, format="%.2f")
    cofins = st.number_input("COFINS (%)", min_value=0.0, max_value=10.0, value=7.6, step=0.1, format="%.2f")

    icms_st = st.number_input("ICMS-ST (ex: Ceará) (%)", min_value=0.0, max_value=20.0, value=0.0, step=0.5, format="%.2f")
    ipi = st.number_input("IPI (%)", min_value=0.0, max_value=20.0, value=0.0, step=0.5, format="%.2f")
    fundo_rj = st.number_input("Fundo Pobreza RJ (%)", min_value=0.0, max_value=5.0, value=2.0, step=0.5, format="%.2f")

# ========================
# BOTÃO DE SIMULAR E SAÍDA
# ========================
with col_output:
    if st.button("🚀 Simular"):
        # Cálculos
        total_impostos = sum([icms, pis, cofins, ipi, icms_st, fundo_rj])
        valor_impostos = receita * total_impostos / 100
        receita_liquida = receita - valor_impostos
        lucro = receita_liquida - custo
        receita_proj = receita_liquida * (1 + crescimento / 100)
        lucro_proj = receita_proj - custo

        st.markdown("### 📈 Resultados")
        st.markdown(f"- <b>Total de Impostos (%)</b>: <span style='color: red;'>{total_impostos:.2f}%</span>", unsafe_allow_html=True)
        st.markdown(f"- <b>Valor Total de Impostos</b>: R$ {valor_impostos:,.2f}")
        st.markdown(f"- Receita Líquida: R$ {receita_liquida:,.2f}")
        st.markdown(f"- Lucro Atual: R$ {lucro:,.2f}")
        st.markdown(f"- Receita Projetada: R$ {receita_proj:,.2f}")
        st.markdown(f"- Lucro Projetado: R$ {lucro_proj:,.2f}")

        if lucro_proj < 0:
            st.error("🔴 Risco de prejuízo com esse cenário!")
        elif lucro_proj < receita * 0.1:
            st.warning("🟡 Lucro projetado baixo, atenção!")
        else:
            st.success("🟢 Cenário saudável de lucro projetado.")

        # Gráfico de projeção
        st.markdown("### 📊 Projeção de Lucro nos Próximos 12 Meses")
        meses = np.arange(1, 13)
        lucro_mensal = [(receita_liquida * ((1 + crescimento / 100) ** (i / 12))) - custo for i in meses]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=meses, y=lucro_mensal, mode='lines+markers', name='Lucro Projetado'))
        fig.update_layout(title="Evolução do Lucro Projetado",
                          xaxis_title="Meses",
                          yaxis_title="Lucro (R$)",
                          height=350)
        st.plotly_chart(fig, use_container_width=True)

        # Regressão para ponto de equilíbrio
        st.markdown("### 📉 Estimativa de Ponto de Equilíbrio")
        vendas_simuladas = np.array([40000, 45000, 50000, 55000, 60000]).reshape(-1, 1)
        lucro_simulado = (vendas_simuladas * (1 - total_impostos / 100)) - custo

        model = LinearRegression()
        model.fit(vendas_simuladas, lucro_simulado)

        a = model.coef_[0][0]
        b = model.intercept_[0]
        ponto_equilibrio_real = -b / a if a != 0 else 0

        st.markdown(f"🔹 Receita mínima estimada para lucro zero: <b>R$ {ponto_equilibrio_real:,.2f}</b>", unsafe_allow_html=True)
        if receita < ponto_equilibrio_real:
            st.error("❗ Receita atual está abaixo do ponto de equilíbrio. Risco de prejuízo.")
        else:
            st.info("✅ Receita atual está acima do ponto de equilíbrio. Cenário sustentável.")
