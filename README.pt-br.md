# CreditGuard: Aplicativo para Detectar Inadimplência
[![English version](https://img.shields.io/badge/lang-en-red.svg)](README.md)
&nbsp;&nbsp;
[![Portuguese version](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md)

`CreditGuard` é um aplicativo para analisar aplicações de empréstimos e com base em dados tomar uma decisão de emprestar ou não ao aplicante. O Aplicativo usa modelos preditivos para determinar se o aplicante é mais provável de adimplir com empréstimo.

O modelo de aprendizado de máquina escolhido foi o `Random Forest` que foi treinado com base de dados de [laotse/credit-risk-dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset). Para saber um pouco mais obre o projeto leia [aqui o notebook](/docs/notebook/notebook_default_loan.pt-br.ipynb).

Projeto desenvolvido para fins da avaliação do curso `Deploy Inteligente: Sistemas com Modelos Preditivo` da Faculdade SENAC Pernambuco.

## Arquitetura em Microsserviços

O projeto foi desenvolvido com uma arquitetura em microsserviços, com os seguintes componentes:

### 1. `backend`
- O componente `backend` é responsável por toda a lógica de negócios, incluindo a exposição de APIs, autenticação, autorização, e o gerenciamento de dados.

### 2. `frontend`
- O componente `frontend` é responsável pela interface de usuário, oferecendo uma experiência interativa e responsiva para os usuários finais. Ele se comunica com o `backend` por meio de APIs.

### 3. `etl`
- O componente `etl` é responsável pela **extração**, **transformação**, e **carga** dos dados na base de dados. Além disso, é responsável por corrigir e limpar dados, realizando as seguintes transformações:
    - **Correção das Idades**:
      - Identificou-se que havia registros de pessoas com idades inviáveis, como 140 anos. Com base na premissa de que ninguém deveria ter mais de 115 anos, as idades dos registros com valores excessivos foram corrigidas.
      - A correção foi feita substituindo as idades desses outliers pela média das idades dos 5 registros mais semelhantes, utilizando o algoritmo KNN.
    - **Imputação de Dados Faltantes**:
      - Para os dados ausentes, foi aplicada uma imputação da média dos 5 registros mais próximos, utilizando o algoritmo KNN.
    - **Transformação de Variáveis Categóricas**:
      - As variáveis categóricas, tanto ordinais quanto nominais, foram transformadas utilizando a técnica One-Hot-Encoding (para variáveis nominais) e Label Encoding (para variáveis ordinais).
    - **Escalonamento de Variáveis**:
      - As variáveis contínuas e discretas foram escaladas para otimizar o aprendizado do modelo. A técnica utilizada foi a normalização/standardização, que foi salva no componente `etl` para ser usada posteriormente.
    - **Salvar o Modelo de Escalamento**:
      - O modelo de escalamento foi treinado e salvo localmente para ser reutilizado posteriormente nas transformações.
    - **Observação**: O componente `etl` também é responsável por salvar o modelo de escalamento das variáveis.

    Para mais detalhes sobre o funcionamento do componente `etl`, leia o documento [aqui](/etl/README.pt-br.md).

### 4. `ml`
- O componente `ml` é responsável por treinar o modelo de aprendizado de máquina e salvá-lo localmente. Ele é alimentado pelos dados transformados pelo componente `etl` e realiza as predições com base no modelo treinado.

## Estrutura do projeto

```plaintext
├── backend/                        # Backend
├── docs/                           # Project documents (ex: diagrams)
├── dataset/                        # data repository, store raw, trusted, features and logs
├── ml/                             # ML training code, store ml model and scaler
├── etl/                            # ETL code
├── frontend/                       # Project documents (ex: diagrams)
├── .gitignore
├── README.md                       # Main documentation
└── README.pt-br.md  
```

## Requerimentos

## Como usar

## Licença