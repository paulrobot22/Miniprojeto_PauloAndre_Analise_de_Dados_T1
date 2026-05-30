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