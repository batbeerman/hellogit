import pandas as pd


#Q1
data = {'Name':['Gaurav', 'Kaustubh'],'Age':[22,21],'mail id':['gaurav@gmail.com','kaushtubh@gmail.com'],'phone no':['999999','8888888']}
df = pd.DataFrame(data)
df.loc[2]=['Saurav',24,'saurav@gmail.com','lml_scooter']
print(df)


#Q2
df = pd.read_csv('weather.csv')
print(df)
print(df.head(5))
print(df.head(10))
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
print(df.tail(5))
fd = [df['MinTemp'].sum(),
df['MinTemp'].mean(),
df['MinTemp'].median(),
df['MinTemp'].nunique(),
df['MinTemp'].max(),
df['MinTemp'].min()]
print(fd)
