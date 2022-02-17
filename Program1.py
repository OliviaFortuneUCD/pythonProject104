import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#https://www.kaggle.com/sourav2000/marketing-analytics
data = pd.read_csv(r'C:\Users\olivi\PycharmProjects\pythonProject104\marketing_data.csv')


print(data.head())
print(data.info())
print(data.describe())


sns.set_theme(style="darkgrid")
plt.figure(figsize = (15,6))

ax = sns.countplot(x="Year_Birth", data=data)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

 