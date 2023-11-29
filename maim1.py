#Principais índices - Yahoo Finanças

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ativos = ['^BVSP', '^MERV', '^MXX', 'CL=F', 'GC=F', 'BTC-USD', 'CMC200', '^GSPC']

# Defina o intervalo de datas desejado
start_date = '2022-01-01'
end_date = '2023-01-01'

# Crie um DataFrame para armazenar os dados
dados_financeiros = pd.DataFrame()

# Obtenha dados para cada ativo
for ativo in ativos:
    dados_ativo = yf.download(ativo, start=start_date, end=end_date)
    dados_financeiros[ativo] = dados_ativo['Close']

# Visualização de séries temporais para cada ativo
dados_financeiros.plot(figsize=(12, 8))
plt.title('Preços de Fechamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend(ativos)
plt.show()

# Matriz de correlação
correlacao = dados_financeiros.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Matriz de Correlação')
plt.show()

