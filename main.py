# How to Multiply two or more Columns in Pandas

import pandas as pd

df = pd.DataFrame({
    'price': [10, 20, 30, 40],
    'amount': [2, 4, 5, 6],
    'product': ['apple', 'pear', 'apple', 'banana']
})

print(df)

df['total'] = df['price'] * df['amount']

print('-' * 50)

print(df)
