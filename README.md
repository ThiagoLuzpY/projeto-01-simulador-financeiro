# 💰 Simulador de Cenários Financeiros – v1.1

Este projeto foi desenvolvido como parte de uma série prática de aplicações úteis para o ambiente corporativo, com foco em análise de dados e visualização interativa. Esta versão avançada permite simular diferentes cenários financeiros com **impostos discriminados por tipo**, possibilitando uma análise mais fiel à realidade empresarial.

---

## 🎯 Objetivo

Permitir a análise de rentabilidade e impacto de variáveis financeiras sobre o lucro líquido de uma empresa, simulando cenários com:

- Receita Bruta  
- Custo Total  
- Impostos individualizados (ICMS, PIS, COFINS, etc)  
- Crescimento ou retração prevista (%)

---

## 🛠 Tecnologias Utilizadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – Interface web simples e rápida
- [Pandas](https://pandas.pydata.org/) – Manipulação de dados
- [Plotly](https://plotly.com/python/) – Visualizações interativas
- [Scikit-learn](https://scikit-learn.org/) – (Previsto para expansões futuras)

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
v1.1 – Adição de impostos discriminados (ICMS, ICMS-ST, PIS, COFINS, IPI, Fundo de Pobreza RJ) com cálculo automático e resultados projetados.

Desenvolvido por Thiago Luz • Todos os direitos reservados © 2025


---

### ✅ Após isso:

Execute os comandos Git para versionar e subir para o GitHub:

```bash
git add .
git commit -m "Versão 1.1 – Simulador com impostos discriminados"
git push