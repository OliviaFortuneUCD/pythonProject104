import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# https://www.kaggle.com/sourav2000/marketing-analytics
data = pd.read_csv(r'C:\Users\olivi\PycharmProjects\pythonProject104\marketing_data.csv')

print(data.head())
print(data.info())
print(data.describe())

s1 = sns.FacetGrid(data = data ,row = 'Education',height=3,
    aspect=2)
s2 = s1.map(sns.countplot,'Marital_Status')
plt.xticks(rotation = 145)
plt.show()
