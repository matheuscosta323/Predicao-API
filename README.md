# Sistema de Predição de Aprovação Acadêmica

Este projeto é uma aplicação web desenvolvida com **Flask** que utiliza um modelo de Machine Learning (**SVM - Support Vector Machine**) para prever a aprovação de alunos com base em dados acadêmicos e demográficos.

## 📂 Estrutura do Projeto
A organização dos arquivos segue as melhores práticas de desenvolvimento para garantir a modularidade e facilidade de manutenção:

```text
/projeto
├── app.py              # Ponto de entrada da aplicação Flask
├── classifier.py       # Lógica de predição e integração com o modelo
├── model.py            # Script de treinamento do modelo
├── requirements.txt    # Dependências do projeto
├── models/             # Pasta contendo o modelo (.pkl)
├── templates/          # Arquivos HTML (Frontend)
└── instances/          # Base de dados (CSV)

🚀 Como rodar o projeto
Siga os passos abaixo no seu terminal (VS Code):

1. Instalação das dependências
Instale as bibliotecas necessárias para o funcionamento do ambiente:

Bash
pip install -r requirements.txt

2. Gerar o Modelo
Caso o arquivo modelo_aprovacao.pkl ainda não tenha sido gerado na pasta models/, execute o script de treinamento para processar os dados e salvar o modelo:

Bash
python model.py

3. Iniciar a Aplicação
Execute o servidor Flask para subir a interface web:

Bash
python app.py

Após executar, o terminal informará um link (geralmente http://127.0.0.1:5000). Acesse este link no seu navegador para utilizar o sistema.

🛠 Tecnologias Utilizadas
Linguagem: Python

Web Framework: Flask

Machine Learning: Scikit-Learn (SVM)

Manipulação de Dados: Pandas

Serialização de Modelo: Joblib