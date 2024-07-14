import pandas as pd

data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago'],
    'Sales': [200, 150, 300, 100]
}
df = pd.DataFrame(data)

grouped_df = df.groupby('City').sum()
print("Grouped and Aggregated Data:\n", grouped_df)