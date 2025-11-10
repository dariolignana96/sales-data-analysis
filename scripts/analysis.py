import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simuliamo un dataset di esempio
np.random.seed(42)
data = {
    'Product': np.random.choice(['A', 'B', 'C'], 100),
    'Sales': np.random.randint(100, 5000, 100),
    'Quantity': np.random.randint(1, 50, 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
}
df = pd.DataFrame(data)

# Salviamo il dataset
df.to_csv('data/sales_data.csv', index=False)

# Overview dataset
print("=== DATASET OVERVIEW ===")
print(f"Shape: {df.shape}")
print(df.head())
print(df.describe())

# Visualizzazioni
plt.figure(figsize=(10,6))
sns.barplot(x='Product', y='Sales', data=df)
plt.title('Vendite medie per Prodotto')
plt.savefig('visualizations/sales_by_product.png')
plt.show()
