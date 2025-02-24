# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# %%
df=pd.read_csv("C:/Users/astit/Downloads/epa-sea-level.csv")
df.head()

# %% [markdown]
# Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
# 

# %%
plt.figure(figsize=(15,6))
sns.scatterplot(data=df,x="Year",y="CSIRO Adjusted Sea Level",c="red",edgecolor="black")
plt.show()

# %% [markdown]
# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050

# %%

slope, intercept, r_value, p_value, std_err=stats.linregress(df["Year"],df["CSIRO Adjusted Sea Level"])


print(f"y = {slope : 0.3f}*x {intercept : 0.3f}\n\nr_value: {r_value : 0.3f}\n\np_value: {p_value : 0.3f}")

# %%
year=np.array(df["Year"])
year_extend=np.array([2025,2030,2040,2050])
year=np.concatenate((year,year_extend))


# %%
def predict(x):
    y=slope*x+intercept
    return y

predicted_values=np.array(predict(year))
predicted_values

# %%
plt.figure(figsize=(15,6))
sns.scatterplot(data=df,x="Year",y="CSIRO Adjusted Sea Level",c="red",edgecolor="black",label="Given data")

plt.plot(year,predicted_values,color="black",label="reg line")
plt.legend()
plt.show()


