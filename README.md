# 🎓 Bootcamp TOTVS - Portfólio de Projetos de Dados

Este repositório foi criado para centralizar todos os projetos práticos e desafios desenvolvidos por mim durante o Bootcamp da DIO em parceria com a TOTVS. O objetivo é aplicar conceitos do mundo real de Engenharia de Dados, Ciência de Dados e Inteligência Artificial utilizando Python.

---

## 🛠️ Projeto 1: Pipeline ETL com Python e Pandas

### 📝 Descrição do Projeto
Este projeto simula um cenário real de inteligência de negócios, onde foi desenvolvido um pipeline de **ETL (Extract, Transform, Load)** para automatizar a criação de mensagens personalizadas de investimentos e retenção para clientes, baseando-se no saldo atual de cada um.

Para contornar a indisponibilidade de APIs externas e focar na arquitetura de dados e na manipulação local, o projeto foi desenhado utilizando arquivos como fonte e destino.

### 🔄 Como o Pipeline Funciona:
1. **Extract (Extração):** Leitura de uma base bruta de clientes (`clientes.csv`) contendo informações de ID, Nome, Saldo e Tipo de Cartão, utilizando a biblioteca **Pandas**.
2. **Transform (Transformação):** Aplicação de regras de negócio em Python para analisar o saldo de cada cliente e gerar uma mensagem personalizada de marketing direcionada (ex: recomendação de Renda Fixa, Renda Variável ou Reserva de Emergência).
3. **Load (Carregamento):** Exportação e salvamento dos dados transformados em um novo arquivo estruturado (`clientes_com_mensagem.csv`), otimizado com codificação (`utf-8-sig`) e separadores (`;`) para abertura imediata no Microsoft Excel, sistemas de ERP ou ferramentas de BI.

### 📂 Estrutura dos Arquivos do Projeto 1
* `etl_projeto.py`: Código-fonte em Python com as três etapas do pipeline.
* `clientes.csv`: Arquivo com os dados brutos de entrada.
* `clientes_com_mensagem.csv`: Arquivo final gerado após o processamento do pipeline.

### 🚀 Tecnologias Utilizadas
* **Python 3**
* **Pandas** (Manipulação e análise de dados)
