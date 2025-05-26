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
