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



# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="Income", y="Country", data=data,
            label="Total", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="Income", y="Country", data=data,
            label="What Ever", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)