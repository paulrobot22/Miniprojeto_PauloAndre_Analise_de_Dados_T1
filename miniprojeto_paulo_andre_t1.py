# =============================================================
# MINI-PROJETO - ANÁLISE EXPLORATÓRIA DE DADOS - VAREJO
# Aluno: Paulo André Monteiro
# Turma: Análise de Dados com Python T1
# =============================================================

# -----------------------------------------------
# SPRINT 1 - IMPORTAÇÃO DOS DADOS
# -----------------------------------------------

import pandas as pd

# Carrega o arquivo CSV com separador ponto e vírgula
df = pd.read_csv(r'C:\Users\Paulo André\Documents\GitHub\Miniprojeto_PauloAndre_Analise_de_Dados_T1\Base Varejo.csv', sep=';', encoding='utf-8')

# Exibe informações básicas da base
print("=" * 50)
print("SPRINT 1 - IMPORTAÇÃO DOS DADOS")
print("=" * 50)
print(f"\nNúmero de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")
print(f"\nColunas e tipos de dados:")
print(df.dtypes)
print(f"\nPrimeiras 5 linhas:")
print(df.head())    

# -----------------------------------------------
# SPRINT 2 - VERIFICAÇÃO DE PROBLEMAS NA BASE
# -----------------------------------------------

print("\n" + "=" * 50)
print("SPRINT 2 - VERIFICAÇÃO DE PROBLEMAS")
print("=" * 50)

# Remove colunas Unnamed (vazias/sem sentido)
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
print(f"\nColunas após remover 'Unnamed': {list(df.columns)}")

# Verifica valores nulos por coluna
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Verifica duplicatas
duplicatas = df.duplicated().sum()
print(f"\nNúmero de linhas duplicadas: {duplicatas}")

# Verifica categorias vazias (strings vazias)
print("\nValores vazios (strings) por coluna de texto:")
colunas_texto = ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']
for col in colunas_texto:
    vazios = (df[col].str.strip() == '').sum()
    print(f"  {col}: {vazios} vazios")

# Verifica datas com formato inválido
print("\nAmostra de valores da coluna DATA:")
print(df['DATA'].value_counts().head())
# -----------------------------------------------
# SPRINT 3 - LIMPEZA DOS DADOS
# -----------------------------------------------

print("\n" + "=" * 50)
print("SPRINT 3 - LIMPEZA DOS DADOS")
print("=" * 50)

# 1. Removendo duplicatas
registros_antes = df.shape[0]
df = df.drop_duplicates()
registros_depois = df.shape[0]
print(f"\nDuplicatas removidas: {registros_antes - registros_depois}")
print(f"Registros restantes: {registros_depois}")

# 2. Convertendo DATA para datetime
# Justificativa: necessário para análises temporais e ordenação por data
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(f"\nColuna DATA convertida para datetime.")
print(f"Tipo atual: {df['DATA'].dtype}")
print(f"Data mínima: {df['DATA'].min()}")
print(f"Data máxima: {df['DATA'].max()}")

# 3. Preenchendo categorias vazias com 'Sem Categoria'
# Justificativa: manter registros sem perder informações das outras colunas
for col in ['PR_CAT', 'CL_SEG', 'CL_GENERO', 'PR_NOME']:
    df[col] = df[col].apply(lambda x: 'Sem Categoria' if str(x).strip() == '' else x)

print(f"\nCategorias vazias preenchidas com 'Sem Categoria'.")

# 4. Exibe tipos de dados após limpeza
print(f"\nTipos de dados após limpeza:")
print(df.dtypes)
# -----------------------------------------------
# SPRINT 4 - ESTATÍSTICAS DESCRITIVAS
# -----------------------------------------------

print("\n" + "=" * 50)
print("SPRINT 4 - ESTATÍSTICAS DESCRITIVAS")
print("=" * 50)

# Coluna analisada: CL_FHL = Número de filhos do cliente
print("\nEstatísticas da coluna 'CL_FHL' (Número de filhos):")
print(f"  Contagem : {df['CL_FHL'].count()}")
print(f"  Média    : {df['CL_FHL'].mean():.2f}")
print(f"  Mediana  : {df['CL_FHL'].median():.2f}")
print(f"  Moda     : {df['CL_FHL'].mode()[0]}")
print(f"  Desvio P.: {df['CL_FHL'].std():.2f}")
print(f"  Mínimo   : {df['CL_FHL'].min()}")
print(f"  Máximo   : {df['CL_FHL'].max()}")
print(f"\nQuartis:")
print(df['CL_FHL'].quantile([0.25, 0.50, 0.75]).to_string())
# -----------------------------------------------
# SPRINT 5 - PADRÕES DE AGRUPAMENTO
# -----------------------------------------------

print("\n" + "=" * 50)
print("SPRINT 5 - PADRÕES DE AGRUPAMENTO")
print("=" * 50)

# Agrupamento 1: Compras por Gênero
print("\n--- Agrupamento 1: Total de compras por Gênero ---")
compras_genero = df.groupby('CL_GENERO')['CO_ID'].count().reset_index()
compras_genero.columns = ['Gênero', 'Total de Compras']
compras_genero = compras_genero.sort_values('Total de Compras', ascending=False)
print(compras_genero.to_string(index=False))

# Agrupamento 2: Compras por Categoria de Produto
print("\n--- Agrupamento 2: Total de compras por Categoria ---")
compras_categoria = df.groupby('PR_CAT')['CO_ID'].count().reset_index()
compras_categoria.columns = ['Categoria', 'Total de Compras']
compras_categoria = compras_categoria.sort_values('Total de Compras', ascending=False)
print(compras_categoria.to_string(index=False))

# Agrupamento 3: Compras por Ano
print("\n--- Agrupamento 3: Total de compras por Ano ---")
df['ANO'] = df['DATA'].dt.year
compras_ano = df.groupby('ANO')['CO_ID'].count().reset_index()
compras_ano.columns = ['Ano', 'Total de Compras']
print(compras_ano.to_string(index=False))

# Agrupamento 4: Compras por Estado Civil
print("\n--- Agrupamento 4: Total de compras por Estado Civil ---")
compras_ec = df.groupby('CL_EC')['CO_ID'].count().reset_index()
compras_ec.columns = ['Estado Civil', 'Total de Compras']
compras_ec = compras_ec.sort_values('Total de Compras', ascending=False)
print(compras_ec.to_string(index=False))
# Dicionário de estado civil (fonte: documentação da base)
mapa_ec = {1: 'Casado/União', 2: 'Divorciado', 3: 'Separado', 4: 'Solteiro', 5: 'Viúvo'}
compras_ec['Estado Civil'] = compras_ec['Estado Civil'].map(mapa_ec)
print("\n--- Agrupamento 4 com descrição: ---")
print(compras_ec.to_string(index=False))
# -----------------------------------------------
# SPRINT 6 - CONCLUSÕES E INSIGHTS
# -----------------------------------------------

print("\n" + "=" * 50)
print("SPRINT 6 - CONCLUSÕES E INSIGHTS")
print("=" * 50)

print("""
1. QUALIDADE DOS DADOS
   A base continha 96.553 registros duplicados (11,6% do total),
   removidos para garantir a integridade da análise.

2. PERFIL DE COMPRAS POR GÊNERO
   Clientes do sexo feminino realizaram mais compras (382.427)
   do que masculino (351.020), diferença de ~8%.

3. CATEGORIA MAIS VENDIDA
   Alimentos lidera com 384.197 compras, representando mais
   de 52% do total. Existe também a categoria #N/D (3.228
   registros) que indica inconsistência nos dados de produto.

4. EVOLUÇÃO TEMPORAL
   As vendas cresceram de 2019 a 2021, com pico em 2021
   (216.813 compras). Em 2022 houve queda para 147.727,
   possivelmente por ser um ano incompleto na base.

5. PERFIL FAMILIAR DOS CLIENTES
   A maioria dos clientes não tem filhos (moda = 0), mas
   a média de 1,15 indica que parte significativa tem filhos.
   75% dos clientes têm até 2 filhos.

6. PROBLEMAS REMANESCENTES
   - Coluna #N/D em PR_CAT indica produtos sem categoria definida.
   - Ano de 2022 pode estar incompleto (dados até dezembro/2022).
   - Não há coluna de valor de venda, limitando análise financeira.
""")