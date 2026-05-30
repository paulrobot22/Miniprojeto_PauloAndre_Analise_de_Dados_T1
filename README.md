# Miniprojeto - Análise Exploratória de Dados - Varejo
**Aluno:** Paulo André Monteiro  
**Turma:** Análise de Dados com Python T1  
**Curso:** SCTEC

## Como executar
1. Instale o Python e o pandas (`pip install pandas`)
2. Coloque o arquivo `Base Varejo.csv` na mesma pasta
3. Abra o VS Code na pasta do projeto
4. Execute: `python miniprojeto_paulo_andre_t1.py`

## Sobre o projeto
Análise Exploratória de Dados (AED) aplicada à base de varejo com
830.000 registros de compras em supermercados entre 2019 e 2022.

## Principais Insights
1. A base continha 96.553 duplicatas (11,6%), removidas na limpeza
2. Mulheres realizaram ~8% mais compras que homens
3. Alimentos representa 52% de todas as compras
4. Vendas cresceram de 2019 a 2021, com queda em 2022
5. Maioria dos clientes não tem filhos (moda = 0)
6. Categoria #N/D indica inconsistência nos dados de produto

## Problemas remanescentes
- Categoria #N/D em PR_CAT indica produtos sem categoria válida
- Ano 2022 possivelmente incompleto na base
- Ausência de coluna de valor financeiro das vendas

## Reflexão sobre ETL e Qualidade de Dados
Durante este projeto apliquei o processo de ETL (Extract, Transform, Load)
na prática. Primeiro extraí os dados brutos do arquivo CSV, depois os
transformei ao remover duplicatas, converter a coluna de datas que estava
como texto para o formato datetime, eliminar colunas sem sentido e tratar
categorias inconsistentes. Por fim carreguei o DataFrame limpo para as
análises e agrupamentos.

Aprendi que a qualidade dos dados é fundamental: dos 830.000 registros
originais, 11,6% eram duplicatas que poderiam distorcer qualquer análise.
Dados sujos geram conclusões erradas e prejudicam decisões de negócio.
Por isso a etapa de limpeza é tão importante quanto a análise em si.