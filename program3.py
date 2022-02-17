import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# https://www.kaggle.com/sourav2000/marketing-analytics
data = pd.read_csv(r'C:\Users\olivi\PycharmProjects\pythonProject104\market.csv')

plt.figure(figsize = (15,6))

# creating a new feature of customer's age
data['Age'] = 2022-data['Year_Birth']

sns.histplot(x = 'Age', data = data, element="bars")
plt.title('Distribution of the Age of customers', fontsize = 22)
plt.show()