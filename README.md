# 💸 MyFinn - Gestão de Finanças Pessoais

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

O **MyFinn** é uma aplicação web full-stack desenvolvida para facilitar o controle financeiro diário. O sistema conta com inteligência de estilização dinâmica para cartões de crédito e normalização de texto inteligente para categorização automática de despesas.


---

## 🚀 Funcionalidades Clave

- **Gestão Inteligente de Cartões (CRUD completo):** Cadastro, edição, listagem e exclusão de cartões com detecção automática de bandeira e paleta de cores institucional com base no nome do banco inserido.
- **Registro Automatizado de Gastos:** Cérebro integrado que analisa a descrição inserida, normaliza o texto (ignorando acentos e capitalização) e define dinamicamente o ícone descritivo e a identidade visual da categoria.
- **Cálculo de Fluxo de Caixa Real:** Back-end estruturado em Python que processa dados tipados em strings brasileiras, converte para floats aritméticos e devolve a soma exata formatada para a interface.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Framework Web:** Flask
- **ORM / Banco de Dados:** Flask-SQLAlchemy / SQLite
- **Interface Visual:** HTML5 & Tailwind CSS (Design Moderno / Clean UI)
- **Normalização de Dados:** Biblioteca nativa `unicodedata`

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
Possuir o **Python 3.11+** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/cesarcapelli/my-finn.git](https://github.com/cesarcapelli/my-finn.git)
   cd my-finn
