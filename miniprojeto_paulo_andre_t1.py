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