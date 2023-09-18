# 1) Crie um dataframe conforme a seguinte tabela:
# 
# |produto|preco|
# |-------|-----|
# |cadeira| 50  |
# | mesa  | 200 |
# |torneira|15|
# |cama| 800|
# |abajur|90|
# |porta|450|

import pandas as pd

#Criei a partir de um dicionário:

dict_data = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

df = pd.DataFrame(data=dict_data)
print(df)


