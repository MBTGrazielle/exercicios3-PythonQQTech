# 7) Crie o seguinte dataframe:
# 
# |produto|qtd_vendida|
# |-------|-----|
# |cadeira| 5  |
# | mesa  | 12 |
# |torneira|65|
# |cama| 51|
# |abajur|12|
# |porta|9|
# 
# E faça um merge com o dataframe do exercício 1 para obter o dataframe a seguir:
# 
# |produto| preco |qtd_vendida|
# |-------| ------|-----|
# |cadeira|    50  |5  |
# | mesa  |200 |12 |
# |torneira|15|65|
# |cama| 800|51|
# |abajur|90|12|
# |porta|450|9|
# 

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
print(df)
