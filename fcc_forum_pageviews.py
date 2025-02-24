# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df=pd.read_csv("C:/Users/astit/OneDrive/Documents/fcc-forum-pageviews.csv")
df.head()

# %%
df.info()

# %% [markdown]
# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.

# %%
df.index=df["date"]
df.head()

# %% [markdown]
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

# %%
Page_views=df[(df["value"]>df["value"].quantile(0.975)) | (df["value"]<df["value"].quantile(0.025))]

Page_views.head()

# %% [markdown]
# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.

# %%
def draw_line_chart(df):
    plt.figure(figsize=(19,5))
    plt.plot(df["value"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("views")
    plt.show()

draw_line_chart(df)


# %% [markdown]
# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

# %%
df['date'] = pd.to_datetime(df['date'])

# %%
df_grouped = df.groupby([df['date'].dt.year, df['date'].dt.month])['value'].sum().reset_index(allow_duplicates=True)
df_grouped.columns = ['Year', 'Month', 'Total']
print(df_grouped)

# %%
plt.bar(x=df_grouped["Year"],height=df_grouped["Total"],)
plt.xticks([2016,2017,2018,2019])
plt.xlabel("Year")
plt.ylabel("month")
plt.show()


