<h1 align="center">🧮 Calculadora Python</h1>

<p align="center">
  Uma calculadora em linha de comando desenvolvida em Python, com arquitetura modular, suporte a variáveis de ambiente e testes automatizados.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/github/license/Mateusreis197/calculadora-python" alt="License" />
  <img src="https://img.shields.io/badge/Author-Mateusreis197-brightgreen" alt="Author" />
</p>

---

## 📌 Sobre o Projeto

Este projeto foi construído para demonstrar conceitos essenciais de engenharia de software em Python:
- **Modularização de código**: Funções independentes e puras para operações matemáticas.
- **Tratamento defensivo de erros**: Proteção contra divisões por zero e entradas incorretas.
- **Configurações por ambiente**: Uso de `.env` para parametrização sem alterar o código-fonte.
- **Qualidade de código**: Testes unitários com o framework padrão `unittest`.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** `python-dotenv` (gerenciamento de variáveis de ambiente)
- **Testes:** Módulo nativo `unittest`

---

## ⚙️ Pré-requisitos e Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Mateusreis197/calculadora-python.git
   cd calculadora-python
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   ```

---

## 💻 Como Executar

Execute o arquivo principal no terminal:
```bash
python calculadora_python.py
```

---

## 🧪 Como Rodar os Testes

Para garantir que todas as funções estão operando conforme esperado, execute:
```bash
python -m unittest test_calculadora.py
```

---

## 👨‍💻 Autor

Desenvolvido por **Mateus Reis**.

- **GitHub:** [@Mateusreis197](https://github.com/Mateusreis197)
- **LinkedIn:** *(adicione o link do seu perfil aqui)*