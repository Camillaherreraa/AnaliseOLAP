# Projeto OLAP de Vendas no Varejo

## Visão Geral

Este projeto tem como objetivo demonstrar a aplicação de técnicas de OLAP (Processamento Analítico Online) para análise de dados de vendas no varejo. OLAP é uma abordagem que permite a análise multidimensional de grandes volumes de dados, facilitando a tomada de decisões estratégicas.

## O que foi feito no projeto

- Foi criada uma base de dados simulada com informações típicas de um sistema de varejo, incluindo categorias de produtos, produtos, lojas, funcionários, clientes, fornecedores, vendas, itens de venda, estoque, compras, avaliações e promoções.
- Os dados foram organizados em tabelas relacionais, conforme demonstrado no arquivo `inserts.md`, que contém os comandos SQL para popular a base de dados.
- No script `olap.py`, os dados foram carregados em DataFrames do pandas para facilitar a manipulação e análise.
- Os dados foram integrados (merge) para formar um conjunto completo que relaciona vendas, produtos, categorias e lojas.
- Foram implementadas funções para realizar consultas OLAP, agregando as vendas por diferentes dimensões:
  - Por loja
  - Por categoria de produto
  - Por produto (top 10 produtos mais vendidos)
  - Por cidade
  - Por estado
- Também foram criadas visualizações gráficas utilizando a biblioteca matplotlib para facilitar a interpretação dos dados:
  - Gráficos de barras para vendas totais por loja, categoria, cidade e estado.
  - Gráfico de barras para os 10 produtos mais vendidos em quantidade.
  - Gráfico 3D de dispersão mostrando a relação entre dia do mês, quantidade vendida e valor total das vendas.

## Como funciona o OLAP neste projeto

OLAP permite analisar dados de forma rápida e flexível, explorando diferentes perspectivas e níveis de detalhe. Neste projeto:

- Os dados de vendas são analisados em múltiplas dimensões (loja, categoria, produto, localização).
- As funções de agregação somam valores de vendas e quantidades para fornecer insights consolidados.
- As visualizações ajudam a identificar padrões, tendências e pontos fortes ou fracos nas vendas.
- O gráfico 3D oferece uma visão mais complexa, relacionando tempo, volume e valor das vendas.

## Tecnologias utilizadas

- Python 3
- pandas para manipulação e análise de dados
- matplotlib para visualização gráfica
- SQL para estruturação e povoamento da base de dados

## Como usar

Execute o script `olap.py` para visualizar os resultados das análises e os gráficos gerados. O script imprime resumos das vendas e exibe gráficos que facilitam a compreensão do desempenho das vendas em diferentes dimensões.

---

Este projeto serve como um exemplo prático de como aplicar OLAP para análise de dados de vendas no varejo, auxiliando na tomada de decisões baseadas em dados.


Manual de Uso do Projeto OLAP de Vendas no Varejo

## Introdução

Este manual tem como objetivo orientar o usuário sobre como utilizar o projeto OLAP de vendas no varejo, que realiza análises multidimensionais dos dados de vendas para apoiar a tomada de decisões estratégicas.

## Requisitos

- Python 3 instalado
- Bibliotecas Python: pandas, matplotlib
- Ambiente para execução de scripts Python (ex: terminal, VSCode, Jupyter Notebook)

## Estrutura do Projeto

- `inserts.md`: Contém os comandos SQL para povoar a base de dados relacional com dados de exemplo.
- `olap.py`: Script Python que carrega os dados, realiza análises OLAP e gera visualizações gráficas.
- `README.md`: Documentação geral do projeto.
- `MANUAL_DE_USO.md`: Este manual de uso.

## Passo a Passo para Utilização

### 1. Preparação da Base de Dados

- Utilize o arquivo `inserts.md` para criar e popular a base de dados relacional em seu sistema de gerenciamento de banco de dados (SGBD) preferido.
- Execute os comandos SQL na ordem apresentada para garantir a integridade dos dados.

### 2. Configuração do Ambiente Python

- Instale as bibliotecas necessárias, caso ainda não tenha:
  ```
  pip install pandas matplotlib
  ```
- Certifique-se de que o Python está configurado corretamente em seu ambiente.

### 3. Execução do Script OLAP

- Abra o terminal ou ambiente de desenvolvimento.
- Navegue até o diretório do projeto.
- Execute o script `olap.py`:
  ```
  python olap.py
  ```
- O script irá carregar os dados simulados, realizar as análises e exibir os resultados no console.
- Serão exibidos gráficos que ilustram as vendas por loja, categoria, produto, cidade e estado, além de um gráfico 3D de dispersão das vendas.

### 4. Interpretação dos Resultados

- Os dados impressos no console mostram as somas totais de vendas e quantidades vendidas agrupadas por diferentes dimensões.
- Os gráficos facilitam a visualização dos dados, permitindo identificar tendências, produtos mais vendidos, lojas com melhor desempenho, entre outros insights.
- O gráfico 3D mostra a relação entre o dia do mês, quantidade vendida e valor total das vendas, oferecendo uma visão mais detalhada do comportamento das vendas ao longo do tempo.

## Personalização e Extensão

- É possível adaptar o script `olap.py` para carregar dados reais de sua base de dados, substituindo os DataFrames simulados.
- Novas análises e visualizações podem ser adicionadas conforme a necessidade.
- O projeto pode ser integrado a dashboards ou sistemas de BI para uso corporativo.

## Suporte e Dúvidas

Para dúvidas ou suporte, entre em contato com o responsável pelo projeto ou consulte a documentação das bibliotecas utilizadas.

---

Este manual visa garantir que o usuário possa utilizar o projeto de forma eficiente e aproveitar ao máximo as análises OLAP implementadas.
