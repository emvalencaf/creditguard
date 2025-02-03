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
    - **Observação**: O componente `etl` também é responsável por salvar o modelo que colocam as variáveis em uma mesma escala.

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
### Configurando o módulo `etl`
1. O primeiro passo é preparar os dados usando o *script* do módulo de `etl`.
2. Para isso baixe no `kaggle` a base de dados ([clique aqui](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)) e crie em sua na raiz do projeto o diretório `dataset/raw` e salve o arquivo `csv`
  - Você pode personalizar o destinos dos dados do processo de `etl` criando um arquivo `.env` no diretório `etl` e configurando as seguintes variáveis:
    - `LOG_DIRECTORY`: variável responsável por determinar o local em que serão salvos os logs do processo de `etl`, por definição ele é `../dataset/logs/etl`
    - `ML_ARTIFACTS_DIRECTORY`: variável responsável por determinar o local em que será  salvo o modelo `scale` responsável por manter numa mesma escala todas as `features` da base de dados. Por padrão seu valor é `../ml/artifacts/models`
    - `TARGET_PARTITION`: variável responsável por determinar o local em que será salvo as variáveis alvo da base de dados, no caso a variável `loan_status`. Por padrão seu valor é "../dataset/features/"
    - `FEATURE_PARTITION`: variável responsável por determinar o local em que será salvo as features da base de dados. Por padrão seu valor é `../dataset/features`
    - `TRUSTED_PARTITION`: variável responsável por determinar o local em que será salvo os dados pré-processados. Por padrão seu valor é `../dataset/trusted`
    - `RAW_PARTITION`: variável responsável por determinar o local em que estar a base de dados. Por padrão seu valor é `../dataset/raw/credit_risk_dataset.csv`. Observe o nome da base de dados, ou use um coringa, por exemplo `../dataset/raw/*`
    - **Observação**: é importante atentar-se que o código do módulo de `etl` será executado no diretório do etl, portanto, `../` vai salvar na raiz do projeto. Nesse caso, se for omitido o `../`, os dados serão salvos dentro do diretório `etl`.
3. Configurado o ambiente de execução do módulo de `etl` você deverá usar os seguintes comandos:
  1. `cd ./etl`: abrir o terminal dentro do diretório `etl`.
  2. `python -m venv .venv`: cria um ambiente virtual à nível de projeto.
  3. `.venv/Scripts/activate`: ativa o ambiente virtual à nível de projeto.
  4. `pip install -r requirements.txt`: baixa todas as dependências necessárias para rodar o módulo `etl`.
  3. `python main.py`: executar o processo de `etl`.
  4. `deactivate`: desativa o ambiente virtual do módulo `etl`.
  5. `cd ..`: para voltar a raiz do projeto.
### Configurando o módulo `ml`
4. Agora que você tem as features e os targets para o treinamento do modelo de machine learning, você deverá configurar o módulo de machine learning.
5. Vá ao diretório `ml` e configure o ambiente do módulo criando o arquivo `.env` no diretório `ml`:
  - `TARGET_PARTITION`: variável responsável por indicar o caminho em que está os dados com os dados da variável alvo. Por padrão o seu valor é `../dataset/features/*/*/*/target-*.csv`.
  - `FEATURE_FEATURE`: variável responsável por indicar o caminho em que está os dados com os dados da `feature`. Por padrão o seu valor é `../dataset/features/*/*/*/feature-*.csv`
  - `MODEL_PARTITION`: variável responsável por indicar o caminho em que será salvo o modelo de machine learning treinado. Por padrão o seu valor é `./artifacts/models`.
  - `MODEL_ALG`: variável responsável por indicar qual é o algoritmo do modelo de machine learning está sendo usado para o treinamento. por padrão seu valor é `rf`
  - `MODEL_VERSION`: variável responsável por indicar qual é a versão do modelo de machine learning. Por padrão seu valor é `1.0.0`.
  - `LOG_DIRECTORY`: variável responsável por indicar qual é o lugar em que serão salvos os logs do treinamento. Por padrão seu valor é `../dataset/logs/training`
  - **Observação**: os dados são salvos pelo módulo `etl` seguindo a seguinte convenção: `{partição}/YYYY/MM/DD/{timestamp}.csv`. Os dados de feature e target seguem a seguinte convenção: `features/YYYY/MM/DD/{target|feature}-{timestamp}.scv`
  - **Observação 2**: o modelo é salvo com a seguinte convenção de nome `{MODEL_ALG}-{MODEL_VERSION}-{timestamp}.pkl`
6. Configurado o ambiente de execução do módulo de `ml` você deverá usar os seguintes comandos:
  1. `cd ./ml`: abrir o terminal dentro do diretório `ml`.
  2. `python -m venv .venv`: cria um ambiente virtual à nível de projeto.
  3. `.venv/Scripts/activate`: ativa o ambiente virtual à nível de projeto.
  4. `pip install -r requirements.txt`: baixa todas as dependências necessárias para rodar o módulo `ml`.
  3. `python main.py`: executar o processo de `ml`.
  4. `deactivate`: desativa o ambiente virtual do módulo `ml`.
  5. `cd ..`: para voltar a raiz do projeto.
### Configurando o módulo `backend`
7. Com os dis modelos - para predição e para manter na mesma escala as features - é possível configurar o `backend` da aplicação.
8. Vá ao diretório `backend` e crie um arquivo `.env` no diretório e configure as seguintes variáveis:
  - `API_V_STR`: responsável por determinar os sufixos dos endpoint. Por padrão tem o valor `/api/v1`.
  - `DB_URL`: responsável por determinar a conexão com o banco de dados. Por padrão tem o valor `localhost:5432/creditguard_db` (função não implementada).
  -``ENVIRONMENT``: responsável por determinar qual é o ambiente do backend, se é de produção ou desenvolvimento. Por padrão seu valor é `DEVELOPMENT`. Caso o valor seja colocado `PRODUCTION` será necessário declarar as variáveis de autenticação do google drive.
  -``GOOGLE_API_PROJECT_ID``: variável obrigatório para quando configurado o projeto do backend para produção. Ela é necessária para chamar a api do google drive e é útil para fazer o deploy do projeto.
  -``GOOGLE_API_SERVICE_ID``:  variável obrigatório para quando configurado o projeto do backend para produção. Ela é necessária para chamar a api do google drive e é útil para fazer o deploy do projeto.
  -``GOOGLE_API_SERVICE_EMAIL``: variável obrigatório para quando configurado o projeto do backend para produção. Ela é necessária para chamar a api do google drive e é útil para fazer o deploy do projeto.
  -``GOOGLE_API_SERVICE_PRIVATE_KEY_ID``: variável obrigatório para quando configurado o projeto do backend para produção. Ela é necessária para chamar a api do google drive e é útil para fazer o deploy do projeto.
  -``GOOGLE_API_SERVICE_PRIVATE_KEY``: variável obrigatório para quando configurado o projeto do backend para produção. Ela é necessária para chamar a api do google drive e é útil para fazer o deploy do projeto.
  - ``BACKEND_PORT``: variável responsável por determinar qual porta será executado o projeto. Por padrão seu valor é : 8080.
  - ``BACKEND_HOST``: variável responsável por determinar qual é o host do backend. Por padrão seu valor é: `localhost`
  - ``MODEL_ARTIFACT_URI``: variável responsável por determinar qual é o caminho para ler o modelo treinado. Por padrão seu valor é: `../ml/artifacts/models/rf-1.0.0-*.pkl` - é recomendável que você veja qual é o nome exato do seu modelo.
  - ``SCALER_ARTIFACT_URI``: variável responsável por determinar qual é o caminho para ler o modelo de scaler treinado para colocar as features em uma mesma escala. Por padrão seu valor é: `../ml/artifacts/utils/scaler.pkl`
  - **OBSERVAÇÃO**: em ambiente de produção as variáveis `MODEL_ARTIFACT_URI` e `SCALER_ARTIFACT_URI` devem ser preenchidas com o id dos seus respectivos objetos que estão salvos no google drive.
  - ``FRONTEND_URL``: variável responsável por determinar a url do frontend para fins de coors. Por padrão seu valor é `http://localhost:8501`.
9. Configurado o ambiente de execução do módulo de `backend` você deverá usar os seguintes comandos:
  1. `cd ./ml`: abrir o terminal dentro do diretório `backend`.
  2. `python -m venv .venv`: cria um ambiente virtual à nível de projeto.
  3. `.venv/Scripts/activate`: ativa o ambiente virtual à nível de projeto.
  4. `pip install -r requirements.txt`: baixa todas as dependências necessárias para rodar o módulo `backend`.
  3. `fastapi run main.py`: executar o backend. Quando quiser fechar o backend aperte `crt+c` ou feche o terminal.
  4. `deactivate`: desativa o ambiente virtual do módulo `backend`.
  5. `cd ..`: para voltar a raiz do projeto.
### Configurando o módulo `frontend`
10. Mantenha o `backend` rodando em um terminal e abra outro.
11. Vá ao diretório `frontend` e crie um arquivo `.env` no diretório e configure as seguintes variáveis:
  - `BACKEND_URL`: variável responsável por indicar a url da api. Por padrão seu valor é `localhost:8000/api/v1/ml/loan_default`
12.  Configurado o ambiente de execução do módulo de `frontend` você deverá usar os seguintes comandos:
  1. `cd ./ml`: abrir o terminal dentro do diretório `frontend`.
  2. `python -m venv .venv`: cria um ambiente virtual à nível de projeto.
  3. `.venv/Scripts/activate`: ativa o ambiente virtual à nível de projeto.
  4. `pip install -r requirements.txt`: baixa todas as dependências necessárias para rodar o módulo `frontend`.
  3. `streamlit run index.py`: executar o frontend. Quando quiser fechar o frontend aperte `crt+c` ou feche o terminal.
  4. `deactivate`: desativa o ambiente virtual do módulo `frontend`.
  5. `cd ..`: para voltar a raiz do projeto.
## Licença