import pandas as pd

df = pd.read_csv('original.csv', sep=',', header=0)


def cleanup_data(row):
    salary = row['Salary'].replace('$', '')
    salary = float(salary)
    return salary


df['clean_salary'] = df.apply(cleanup_data, axis=1)


# x = df.groupby('gender')['clean_salary'].mean()
# print(x)


def female_salary(row):
    if row['gender'] == 'Female':
        return row['clean_salary']


df['female_salary_avg'] = df.apply(female_salary, axis=1)


def male_salary(row):
    if row['gender'] == 'Male':
        return row['clean_salary']


df['male_salary_avg'] = df.apply(male_salary, axis=1)

y = df.groupby('Job Title')['clean_salary', 'male_salary_avg', 'female_salary_avg'].mean()
print(y)
df.to_csv('edited.csv')