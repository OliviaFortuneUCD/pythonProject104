import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# https://www.kaggle.com/sourav2000/marketing-analytics
data = pd.read_csv(r'C:\Users\olivi\PycharmProjects\pythonProject104\market.csv')

grouped = data.groupby(['Country','Education'])
grouped = grouped.agg(np.mean)
print(grouped['Year_Birth'])
