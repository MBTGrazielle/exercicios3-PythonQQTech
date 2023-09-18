# 3) Adicione ao dataframe o produto "tapete" que tem valor 250.

import pandas as pd

dict_data = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

df = pd.DataFrame(data=dict_data)
df.loc[len(df)] = ['tapete', 250]

df = df.sort_values(by='preco', ascending=False)

print(df)