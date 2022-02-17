import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# https://www.kaggle.com/sourav2000/marketing-analytics
data = pd.read_csv(r'C:\Users\olivi\PycharmProjects\pythonProject104\market.csv')

#Change the Dt_Customer field data type to datetime
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], format='%m/%d/%y')
# Change the Income field data type to Float
data["Income"] = data["Income"].str.replace("$","").str.replace(",","")
data["Income"] = data["Income"].astype(float)


# Plot the responses for different events and regions
sns.lineplot(x="Income", y="MntWines",
             hue="Year_Birth",
             data=data)
