# Previsão de Vendas da FabProd

Este projeto tem como objetivo criar um modelo de previsão de vendas para a empresa FabProd, utilizando dados históricos e informações econômicas dos municípios.

# Problema

Considere a empresa FabProd responsável por fabricar e distribuir uma família de produtos de limpeza de veículos para região Sul do Brasil. No entanto, CEO dessa empresa não tem conhecimento do quanto a FabProd pode expandir a distribuição nessa região e nas demais regiões do Brasil. O CEO têm apenas informações sobre as vendas oriundas do ERP, e está interessado em conhecer melhor as possibilidades de expansão dos negócios para FabProd. Ele sabe que existe uma área multidisciplinar (ciência de dados) que pode ajudá-lo, mas ele não sabe como. Considerando esse cenário faça uma demonstração utilizando dados sintéticos como um exemplo de um conjunto de possibilidades. 

Para esse cenário: 
- Inclua aspectos da Análise Exploratória de Dados 
- Um modelo preditivo (disciplina Aprendizagem de Máquina)
- Por outro lado, esclareça que a FabProd precisa valorizar os dados que são gerados internamente e externamente da cadeia produtiva em que a FabProd está inserida (se precisar utilize a metodologia CRISP-DM).

## Passo a passo do processo executado

1. Coleta de dados: Os dados foram coletados de diferentes fontes, as informações demográficas e econômicas dos municípios foram obtidas dos sites oficiais do IBGE e SEINFRA. Os dados históricos das vendas da FabProd foram gerados artificialmente baseado no conjunto de dados coletado.

2. Pré-processamento de dados: Os dados foram limpos, processados e combinados em um único conjunto de dados que inclui informações demográficas, econômicas e de vendas. Os arquivos em Python utilizados para realizar essas etapas são `extract_Pib.py`, `extract_Populacao.py` e `merge_extracted_Final.py`. Os comentários nesses arquivos fornecem detalhes sobre cada etapa do processo.

3. Geração de dados históricos: Um conjunto de dados históricos foi gerado com base nos dados existentes, simulando variações nas vendas e concorrência ao longo de 12 meses.

4. Modelagem e avaliação: Diferentes modelos de regressão foram aplicados ao conjunto de dados históricos para prever as vendas futuras da FabProd. Os modelos foram avaliados com base no erro quadrático médio (MSE) e no coeficiente de determinação (R^2).

## Conclusão
Resultados:

| Modelo             | Erro Quadrático Médio (MSE) | Coeficiente de Determinação (R^2) |
|--------------------|-----------------------------|-----------------------------------|
| Regressão Linear   | 156.84                      | -0.00                             |
| Lasso              | 156.84                      | -0.00                             |
| Ridge              | 156.84                      | -0.00                             |
| Árvore de Decisão  | 6.94                        | 0.96                              |
| Floresta Aleatória | 5.36                        | 0.97                              |
| Gradient Boosting  | 152.37                      | 0.03                              |

Com base nos resultados dos modelos de regressão aplicados para prever as vendas da FabProd, o modelo de Árvore de Decisão e o modelo de Floresta Aleatória apresentaram os melhores desempenhos. O erro quadrático médio (MSE) foi menor e o coeficiente de determinação (R^2) foi maior para ambos os modelos em comparação aos outros modelos testados.

A Árvore de Decisão obteve um MSE de 6,94 e um R^2 de 0,96, enquanto a Floresta Aleatória obteve um MSE de 5,36 e um R^2 de 0,97. Isso indica que a Floresta Aleatória teve um desempenho ligeiramente melhor que a Árvore de Decisão, e ambos os modelos foram capazes de explicar uma grande parte da variância nos dados.

Em contraste, os modelos de Regressão Linear, Lasso e Ridge tiveram um desempenho muito fraco, com R^2 próximo de 0 e MSE significativamente maior. O modelo de Gradient Boosting apresentou um desempenho um pouco melhor que os modelos lineares, mas ainda assim insuficiente quando comparado à Árvore de Decisão e à Floresta Aleatória.

Com base nesses resultados, a FabProd deve considerar o uso do modelo de Floresta Aleatória para prever suas vendas futuras e expansão de mercado para outras regiões do Brasil, uma vez que apresentou o melhor desempenho entre os modelos testados.

# Aluno: João Vitor de Souza Tomio.