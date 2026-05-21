import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example macroeconomic dataset
data = {
    "Gold": [1800, 1815, 1790, 1820, 1835],
    "Oil": [70, 72, 71, 73, 74],
    "SP500": [4200, 4220, 4210, 4250, 4275],
    "InterestRate": [1.5, 1.5, 1.75, 1.75, 2.0]
}

df = pd.DataFrame(data)

# Correlation matrix
corr_matrix = df.corr()

# Heatmap visualization
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

plt.title("Macroeconomic Variables Correlation")
plt.tight_layout()
plt.show()
