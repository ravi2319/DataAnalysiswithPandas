import pandas as pd

df = pd.read_csv('exercise.csv', sep=',', header=0)


def male_bytes(row):
    if row['gender'] == 'Male':
        return row['bytes']


df['male_bytes'] = df.apply(male_bytes, axis=1)


def female_bytes(row):
    if row['gender'] == 'Female':
        return row['bytes']


df['female_bytes'] = df.apply(female_bytes, axis=1)

bytes_per_domain = df.groupby('url')['bytes'].sum()
print(bytes_per_domain)

x = df.groupby('url')['male_bytes', 'female_bytes'].sum()
print(x)

df2 = df.groupby(['country', 'url'])['male_bytes', 'female_bytes'].sum()
print(df2)
