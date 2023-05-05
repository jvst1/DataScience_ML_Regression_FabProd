import pandas as pd

# Define o caminho do arquivo Excel
file_path = "./resources/input/pibmunicipios.xlsx"

# Lê o arquivo Excel usando o engine 'openpyxl'
df = pd.read_excel(file_path, engine='openpyxl')

# Extrai as colunas de interesse do DataFrame
extracted_columns = df[['NomeRegiao', 'SiglaUF', 'NomeUF', 'CodigoMunicipio', 'NomeMunicipio_y', 'ValorBrutoAgropecuaria',
                        'ValorBrutoIndustria',	'ValorBrutoServico1',	'ValorBrutoServico2',	'ValorBrutoTotal',	'ValorImposto', 'PibBruto',	'PibBrutoPerCapita']]

# Salva as colunas extraídas em um arquivo CSV
extracted_columns.to_csv(
    "./resources/processed/extracted_Pib.csv", index=False)
