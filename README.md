# 💰 Simulador de Cenários Financeiros – v1.2

Este projeto foi desenvolvido como parte de uma série prática de aplicações úteis para o ambiente corporativo, com foco em análise de dados, visualização interativa e simulação de cenários financeiros.  
A versão 1.2 traz aprimoramentos visuais e funcionais que permitem uma análise ainda mais intuitiva e profissional.

---

## 🎯 Objetivo

Permitir a análise de rentabilidade e impacto de variáveis financeiras sobre o lucro líquido de uma empresa, simulando cenários com:

- Receita Bruta  
- Custo Total  
- Impostos individualizados (ICMS, PIS, COFINS, ICMS-ST, IPI, Fundo de Pobreza RJ)  
- Crescimento ou retração prevista (%)  
- Projeção de lucro nos próximos 12 meses  
- Estimativa de ponto de equilíbrio com regressão linear  
- Alertas automáticos sobre saúde financeira do cenário

---

## 🛠 Tecnologias Utilizadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – Interface web simples e rápida
- [Plotly](https://plotly.com/python/) – Visualizações interativas
- [NumPy](https://numpy.org/) – Cálculos matemáticos
- [Scikit-learn](https://scikit-learn.org/) – Regressão linear

---

## 📁 Estrutura de Pastas

```plaintext
projeto-01-simulador-financeiro/
├── app.py           # Arquivo principal do sistema
├── README.md        # Descrição do projeto
├── requirements.txt # Dependências do projeto
└── data/            # Pasta para arquivos simulados (futura expansão)


▶️ Como Executar
Clone o repositório:

git clone https://github.com/ThiagoLuzpY/projeto-01-simulador-financeiro.git
cd projeto-01-simulador-financeiro

Ative o ambiente virtual e instale as dependências:

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt


Execute o sistema:

streamlit run app.py


📌 Versão Atual
v1.2 – Interface profissionalizada, projeção mensal com gráfico, cálculo do ponto de equilíbrio com regressão linear, e alertas inteligentes.

Desenvolvido por Thiago Luz • Todos os direitos reservados © 2025


---

### ✅ Após isso:

Execute os comandos Git para versionar e subir para o GitHub:

```bash
git add .
git commit -m "Versão 1.2 – Interface melhorada + regressão + alertas + layout"
git push


---

### ✅ `requirements.txt` atualizado

```txt
streamlit==1.33.0
plotly==5.21.0
numpy==1.26.4
scikit-learn==1.4.2