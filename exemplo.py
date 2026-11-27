import pandas as pd 

idades_listas = [25, 30, 22, 28]

idades_series = pd.Series([25, 30, 22, 28])

# print(f"Lista:\n{idades_listas}\n")
# print(f"Series: \n{idades_series}")

notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])

print(notas['Maria'])     # Acessando a nota de Maria pelo rótulo
print(notas.iloc[2])      # Acessando a nota de Pedro pela posição 
print(notas.mean())       # Calculando a média das notas​
print(notas[notas > 8])   # Filtrando notas maiores que 8​
print(notas.describe())   # Estatísticas descritivas das notas​

# Operações aritméticas e entre duas Séries

# Aumentar todas as notas em 10% de uma vez só 
notas_ajustadas = notas * 1.10 
print(notas_ajustadas) 

# Comparar com uma segunda series 

notas_exame_final = pd.Series([10, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana']) 
diferenca = notas_exame_final - notas_ajustadas 

print(diferenca) 

# DataFrames Lendo Planilhas do Excel

df = pd.read_excel('base_invest.xlsx')  # Lê a planilha Excel da pasta​

print(df.head())                        # Exibe as 5 primeiras linhas