# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# Import the data from medical_examination.csv and assign it to the df variable.

# %%
df=pd.read_csv("medical_examination.csv")
df.head()

# %%
df["height"]=df["height"].astype(float)

# %%
df=df.rename({"ap_hi":"BP_high","ap_lo":"BP_low"},axis=1)

# %% [markdown]
# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

# %%
def bmiover(weight,height):
    bmi=0
    if bmi>25:
        return 1
    else:
        return 0

# %%
df.insert(13,"overweight",bmiover(df["weight"],df["height"]))
df.head()

# %% [markdown]
# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# Draw the Categorical Plot in the draw_cat_plot function.

# %%
def Normalize(x):
    if x>1:
        return 1
    else:
        return 0


# %%
df["cholesterol"]=df["cholesterol"].apply(Normalize)
df["glucose"]=df["glucose"].apply(Normalize)
df.head()

# %%
plt.figure(figsize=(15,10))

plt.subplot(2,2,1)
ax=sns.countplot(data=df,x="cholesterol",hue="cholesterol",edgecolor='black')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.ylabel("No of patients")

plt.subplot(2,2,2)
ax=sns.countplot(data=df,x="glucose",hue="glucose",edgecolor='black')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.ylabel("No of patients")

plt.show()

# %% [markdown]
# Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.

# %%
df_cat = pd.melt(df, id_vars=['id'], value_vars=['cholesterol', 'glucose', 'smoke', 'alco', 'active', 'overweight'])

ax=sns.catplot(data=df_cat,x=df_cat["variable"],y=df_cat["value"],kind="bar",errorbar=None,edgecolor="black",legend="auto")
plt.show()

# %%
df_cat["cardio"]=df["id"]
df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
df_cat

# %% [markdown]
# Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
# 
# 
# diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
# 
# 
# height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
# 
# 
# height is more than the 97.5th percentile
# 
# 
# weight is less than the 2.5th percentile
# 
# 
# weight is more than the 97.5th percentile

# %%
df_heat=df[(df["BP_high"]<df["BP_low"]) | (df["height"]<df["height"].quantile(0.025)) | (df['height']>df["height"].quantile(0.975)) | (df["weight"]<df["weight"].quantile(0.025)) | (df["weight"]<df["weight"].quantile(0.975))]

df_heat.head()

# %% [markdown]
# Calculate the correlation matrix and store it in the corr variable.

# %%
corr=df.corr()

# %% [markdown]
# Generate a mask for the upper triangle and store it in the mask variable.
# 

# %%
mask = np.triu(np.ones_like(corr, dtype=bool))


# %% [markdown]
# Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().

# %%
plt.figure(figsize=(10,5))
sns.heatmap(corr, mask=mask, cmap="coolwarm", annot=True)
plt.xticks(rotation=45)

plt.show()


