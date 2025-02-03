# CreditGuard - Módulo ETL - Conjunto de Dados de Risco de Crédito

## Visão Geral
Este módulo é responsável por extrair, limpar, transformar e salvar dados do conjunto de dados Kaggle: [Conjunto de Dados de Risco de Crédito](https://www.kaggle.com/datasets/laotse/credit-risk-dataset). Ele também seleciona características, normaliza-as, salva o modelo do escalador e armazena as características processadas e o alvo.

## Estrutura do Projeto
```
|__ helpers/
|     |__ calc.py
|     |__ datetime_partition.py
|     |__ logging.py
|     |__ makedir.py
|__ config.py
|__ main.py
|__ requirements.txt
```

## Instalação
Certifique-se de que o Python está instalado. Em seguida, instale as dependências necessárias:

```sh
pip install -r requirements.txt
```

## Detalhes do Módulo
### `helpers/`
#### ``helpers/calc.py``
Este módulo fornece funções para operações matemáticas:

- ``truncate(value: float, decimal_places: int) -> float``: Trunca um valor float para o número especificado de casas decimais sem arredondar.
- ``calculate_expected_loan_percent(df: pd.DataFrame, decimal_places: int = 2) -> pd.Series``: Calcula a porcentagem esperada de ``loan_percent_income`` com base em ``loan_amnt`` e ``person_income``.
#### ``helpers/datetime_partition.py``
Fornece funções utilitárias para gerenciamento de timestamps:

- ``get_datetime_partition() -> str``: Retorna uma partição de diretório com base na data atual (yyyy/mm/dd).
- ``get_timestamp() -> float``: Retorna o timestamp atual.
#### ``helpers/logging.py``
Gerencia a configuração de logs:

- ``get_logging() -> logging.Logger``: Configura e retorna uma instância de logging que armazena logs em diretórios criados dinamicamente.

#### ``helpers/makedir.py``
Garante a existência de diretórios:

- ``ensure_dir(directory: str)``: Cria o diretório especificado se ele não existir.

### ``config.py``
Gerencia as configurações de ambiente usando ``pydantic_settings``:

= Define os caminhos para as partições de dados brutos, confiáveis, características e alvo.
- Define os diretórios para artefatos de ML e logs.

### ``main.py``
Executa o processo ETL:

1. Carrega o conjunto de dados da partição bruta.
2. Limpa inconsistências nos dados:
    - Corrige inconsistências de ``loan_percent_income``.
    - Substitui valores inválidos de ``person_age``.
3. Transforma dados categóricos usando ``OneHotEncoder``.
4. Trata valores ausentes usando ``KNNImputer``.
5. Salva o conjunto de dados confiável.
6. Normaliza características numéricas usando StandardScaler e, em seguida, salva o modelo do escalador.
7. Seleciona características relevantes e separa a variável alvo.
8. Salva os conjuntos de características e alvo processados.

## Executando o Pipeline ETL
Execute o processo ETL rodando:

```sh
python main.py
```
## Arquivos de Saída
- Conjunto de dados confiável: Salvo em ``TRUSTED_PARTITION``.
- Conjunto de características: Salvo em ``FEATURE_PARTITION``.
- Conjunto alvo: Salvo em ``TARGET_PARTITION``.
- Modelo do escalador: Armazenado em ``ML_ARTIFACTS_DIRECTORY/utils/scaler.pkl``.
## Logs
Os logs são gerados dinamicamente e armazenados em ``LOG_DIRECTORY``, seguindo o formato de partição baseado na data.

## Licença
Este projeto é licenciado sob a Licença MIT.