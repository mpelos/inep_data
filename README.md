INEP Data
=========

Sobre
-----

Este projeto foi criado seguindo a seguinte proposta:
https://gist.github.com/rodrigoalmeidaee/6096344

Instalação
----------

`pip install -r requirements.txt`

Importação dos Dados
--------------------

### Dados do ENEM
`python import_enem_data.py <nome_do_arquivo.txt> --workers 2`

Visando aumentar a performance da importação dos dados a opção `--workers` cria a quantidade estipulada de processos.

### Dados da Escola
`python import_school_data.py <nome_do_arquivo.csv>`

Como o arquivo de dados do ENEM não possui o nome das escolas, é usado um arquivo CSV com os seguintes dados:
* 1° coluna: Sigla do estado
* 2° coluna: Código do município da escola
* 3° coluna: Nome do município
* 4° coluna: Código da escola
* 5° coluna: Nome da escola

Inicialização do Servidor Web
-----------------------------

`python inep_data.py`
