import pandas as pd
import numpy as np

# Lendo os arquivos CSV extraídos
populacao = pd.read_csv("./resources/processed/extracted_Populacao.csv")
pib = pd.read_csv("./resources/processed/extracted_Pib.csv")

# Mesclando os dois conjuntos de dados baseado na coluna 'CodigoMunicipio'
dados_finais = pd.merge(populacao, pib, on='CodigoMunicipio', how='inner')

# Selecionando colunas relevantes
dados_finais = dados_finais[['SiglaUF', 'NomeUF', 'NomeRegiao', 'CodigoMunicipio', 'NomeMunicipio_y', 'Populacao', 'ValorBrutoAgropecuaria',
                             'ValorBrutoIndustria', 'ValorBrutoServico1', 'ValorBrutoServico2', 'ValorBrutoTotal', 'ValorImposto', 'PibBruto', 'PibBrutoPerCapita']]

# Gerando valores aleatórios para 'Concorrentes' e 'Vendas'
random_concorrentes = np.random.randint(2, 6, size=len(dados_finais))
random_vendas = np.random.randint(1, 50, size=len(dados_finais))
dados_finais['Concorrentes'] = random_concorrentes
dados_finais['Vendas'] = random_vendas

# Salvando os dados finais mesclados em um arquivo CSV
dados_finais.to_csv("./resources/processed/merged_final.csv", index=False)

# Filtrando o conjunto de dados baseado em 'NomeRegiao'
df_sul = dados_finais[dados_finais['NomeRegiao'] == 'Sul']

# Definindo o número de pontos de dados históricos que você deseja gerar (por exemplo, 12 meses)
num_months = 12

# Criando um DataFrame vazio para armazenar os dados históricos
df_history = pd.DataFrame()

# Gerando dados históricos iterando sobre cada linha no conjunto de dados filtrado
for _, row in df_sul.iterrows():
    for month in range(1, num_months + 1):
        # Criando uma cópia da linha atual
        historical_row = row.copy()

        # Modificando o valor de vendas com base em uma função simples, por exemplo, uma diminuição de 2% ao mês
        historical_sales = historical_row['Vendas'] * (1 - 0.02)**month
        historical_row['Vendas'] = int(round(historical_sales))

        # Modificando o valor de 'Concorrentes' com base em uma função simples
        # Adicionar ou remover concorrentes aleatoriamente com 50% de chance
        change = np.random.choice([-1, 0, 1], p=[0.25, 0.5, 0.25])
        historical_concorrentes = max(
            0, historical_row['Concorrentes'] + change)
        historical_row['Concorrentes'] = int(historical_concorrentes)

        # Adicionando uma nova coluna para o mês
        historical_row['Meses'] = month

        # Anexando a linha histórica ao conjunto de dados históricos
        df_history = pd.concat(
            [df_history, pd.DataFrame(historical_row).T], ignore_index=True)

# Salvando o conjunto de dados históricos em um arquivo CSV
df_history.to_csv('./resources/output/historical_data.csv', index=False)
