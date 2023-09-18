# 8) Crie uma coluna no dataframe do exercício anterior que indique a receita total do produto, após isso, calcule a receita total de todos os produtos e crie uma nova coluna indicando qual a porcentagem de cada produto na receita total.

import pandas as pd

dict_data1 = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

dict_data2 = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'qtd_vendida': [5, 12, 65, 51, 12, 9]
}


df = pd.DataFrame(data=dict_data1)


df2 = pd.DataFrame(data=dict_data2)


df = pd.merge(df,df2, on='produto', how='left')
df.loc[len(df)] = ['tapete', 250,2]
df['receita'] = df['preco'] * df['qtd_vendida']


receita_total = df['receita'].sum()
df['receita_total_produto'] = receita_total

df['porcentagem_receita'] = (df['receita']* 100) / receita_total
print(df)