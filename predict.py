import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Supondo que seus dados estão em um arquivo CSV
# Substitua pelo caminho do seu arquivo de dados
data_file = "./resources/output/historical_data.csv"
df = pd.read_csv(data_file)

# Seleciona as características e a variável alvo
features = ['Populacao', 'PibBrutoPerCapita', 'Concorrentes']
target = 'Vendas'

X = df[features]
y = df[target]

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Escala as características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Cria uma lista de modelos de regressão
models = [
    ('Regressão Linear', LinearRegression()),
    ('Lasso', Lasso()),
    ('Ridge', Ridge()),
    ('Árvore de Decisão', DecisionTreeRegressor(random_state=42)),
    ('Floresta Aleatória', RandomForestRegressor(random_state=42)),
    ('Gradient Boosting', GradientBoostingRegressor(random_state=42))
]

# Inicializa um escritor do Excel
writer = pd.ExcelWriter(
    './resources/output/model_predictions.xlsx', engine='openpyxl')

# Avalia cada modelo usando os dados de teste e exporta os resultados para um arquivo Excel
for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"{name}:")
    print(f"  Erro Quadrático Médio: {mse:.2f}")
    print(f"  Coeficiente de Determinação (R^2): {r2:.2f}\n")

    # Converte as previsões do conjunto de teste em um DataFrame
    y_pred_df = pd.DataFrame(y_pred, columns=[f'Vendas_Previstas_{name}'])
    y_test_df = y_test.reset_index(drop=True)

    # Combina os dados originais do teste com as vendas previstas
    X_test_df = pd.DataFrame(
        scaler.inverse_transform(X_test), columns=features)
    results = pd.concat([X_test_df.reset_index(
        drop=True), y_test_df, y_pred_df], axis=1)

    # Exporta os resultados para uma planilha separada no arquivo Excel
    results.to_excel(writer, sheet_name=name, index=False)

# Salva o arquivo Excel
writer.book.save('./resources/output/model_predictions.xlsx')
