import pandas as pd

df=pd.read_csv("C:/Users/astit/Project free code camp/census income.csv")


total_people=df["age"].count()
print(f"\n\nTotal people: {total_people}\n\n")

df['workclass'] = df['workclass'].str.strip()
df['education'] = df['education'].str.strip()
df['marital-status'] = df['marital-status'].str.strip()
df['occupation'] = df['occupation'].str.strip()
df['relationship'] = df['relationship'].str.strip()
df['sex'] = df['sex'].str.strip()
df['race'] = df['race'].str.strip()




df["education-num"]=pd.to_numeric(df["education-num"],errors="coerce")
df["fnlwgt"]=pd.to_numeric(df["fnlwgt"],errors="coerce")
df["age"]=pd.to_numeric(df["age"],errors="coerce")
df["capital-gain "]=pd.to_numeric(df["capital-gain"],errors="coerce")
df["capital-loss"]=pd.to_numeric(df["capital-loss"],errors="coerce")
df["hours-per-week"]=pd.to_numeric(df["hours-per-week"],errors="coerce")



Race=df.groupby("race")["age"].count()
Race=pd.Series(Race)
print(Race,"\n\n")

print(f"Average age: {df["age"].mean() : 0.3f}\n\n")

df['education'] = df['education'].str.strip()
people_with_bachelors=df[df["education"]=="Bachelors"]["age"].count()
print(f"No of people_with_bachelors :{people_with_bachelors}\n\n")


people_with_bachelors=(people_with_bachelors/total_people)*100
print(f"percentage of people with bachelors : {people_with_bachelors : 0.3f}%\n\n")

df["education-num"]=pd.to_numeric(df["education-num"],errors="coerce")
df['salary'] = df['salary'].str.strip()

per=df[(df["salary"]==">50K") & ((df["education-num"]==13) | (df["education-num"]==16) | (df["education-num"]==14))]["age"].count()

print(f"Percentage of people with advanced education and salary more then 50k: {(per/total_people)*100 : 0.3f}%\n\n")




people=df[(df["salary"]==">50K") & ((df["education"]!="Bachelors") | (df["education"]!="Masters") | (df["education"]!="Doctorate"))]["age"].count()


print(f"Percentage of people without advanced education and salary more then 50k: {(people/total_people)*100 : 0.3f}%\n\n")



min_number_hours=df["hours-per-week"].min()

print(f"Minimum hours person works per week : {min_number_hours}\n\n")


people=df[(df["salary"]==">50K") & (df["hours-per-week"]==df["hours-per-week"].min())]["age"].count()


print(f"percentage of the people who work the minimum number of hours\n\nper week have a salary of more than 50K: {(people/total_people)*100 : 0.3f}%\n\n")



df1=df[df["salary"]==">50K"]
count_of=df1.groupby("native-country")["salary"].count()
country=pd.Series(count_of.sort_values(ascending=False))
print(f"country has the highest percentage of people that earn >50K is : {country.index[0]}\npercentage of people: {(country.iloc[0]/country.sum()*100): 0.3f}%\n\n")



peopleIndia=df["occupation"][df["salary"]==">50K"]
mostPopOcc=peopleIndia.groupby(by=peopleIndia).count().sort_values(ascending=False)

print(f"The most popular occupation for those who earn >50K in India is : {mostPopOcc.index[0]}\n")
