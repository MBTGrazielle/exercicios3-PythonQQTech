# 2) Com o dataframe criado, ordene-o em ordem decrescente de preço.

import pandas as pd

dict_data = {
    'produto': ['cadeira', 'mesa', 'torneira', 'cama', 'abajur', 'porta'],
    'preco': [50, 200, 15, 800, 90, 450]
}

df = pd.DataFrame(data=dict_data)

df = df.sort_values(by='preco', ascending=False)

print(df)