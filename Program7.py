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



Average_salary = data[data["Income"] <= 100000]

sns.set_theme(style="whitegrid")


g = sns.catplot(
    data=Average_salary , kind="bar",
    x="Country", y="Income", hue="Education",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "My header")
g.legend.set_title("")