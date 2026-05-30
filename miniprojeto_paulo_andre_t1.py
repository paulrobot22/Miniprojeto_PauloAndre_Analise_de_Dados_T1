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