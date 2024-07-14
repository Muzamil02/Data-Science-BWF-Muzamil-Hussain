import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

df['City'] = ['New York', 'Los Angeles', 'Chicago']
print("DataFrame with new column:\n", df)