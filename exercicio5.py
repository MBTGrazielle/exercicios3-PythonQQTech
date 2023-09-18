# 5) Salve o dataframe original em um arquivo csv

import pandas as pd

dict_data = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

df = pd.DataFrame(data=dict_data)
df.loc[len(df)] = ['tapete', 250]

df = df.sort_values(by='preco', ascending=False)

caminho_csv = r'C:\Users\980184\Desktop\QQtech\exercicios3-PythonQQtech\arquivo.csv'

df.to_csv(caminho_csv, encoding='latin-1', sep=' ', decimal=',')