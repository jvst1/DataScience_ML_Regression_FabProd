import pandas as pd

# Define o caminho do arquivo Excel
file_path = "./resources/input/codigoMunicipio-nomeMunicipio-Populacao.xlsx"

# Lê o arquivo Excel usando o engine 'openpyxl'
df = pd.read_excel(file_path, engine='openpyxl')

# Extrai as colunas de interesse do DataFrame
extracted_columns = df[['CodigoMunicipio', 'NomeMunicipio', 'Populacao']]

# Salva as colunas extraídas em um arquivo CSV
extracted_columns.to_csv(
    "./resources/processed/extracted_Populacao.csv", index=False)
