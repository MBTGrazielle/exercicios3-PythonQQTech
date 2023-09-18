# 6) Use o pd.read_csv para ler o dataframe salvo anteriormente e adicione a esse dataframe uma coluna "vendas" que representa a quantidade vendida (inicialmente nenhum produto vendido, então o valor será 0 para todas as linhas).

import pandas as pd

dict_data = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

df = pd.DataFrame(data=dict_data)
df['vendas'] = [0, 0, 0, 0, 0, 0]
df.loc[len(df)] = ['tapete', 250,0]

df = df.sort_values(by='preco', ascending=False)
print(df)

caminho_csv = r'C:\Users\980184\Desktop\QQtech\exercicios3-PythonQQtech\arquivo.csv'

df = pd.read_csv(caminho_csv, encoding='latin-1', sep=' ', decimal=',')


