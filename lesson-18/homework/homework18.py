import pandas as pd

so_df = pd.read_csv("tack_overflow_qa.csv")
titanic_df = pd.read_csv("titanic.csv")

# Stack Overflow Tasks
q1 = so_df[pd.to_datetime(so_df['creationdate']) < '2014-01-01']
q2 = so_df[so_df['score'] > 50]
q3 = so_df[(so_df['score'] >= 50) & (so_df['score'] <= 100)]
q4 = so_df[so_df['ans_name'] == 'Scott Boston']
users = ['Scott Boston', 'unutbu', 'Warren Weckesser', 'DSM', 'jezrael']
q5 = so_df[so_df['ans_name'].isin(users)]
so_df['creationdate'] = pd.to_datetime(so_df['creationdate'])
q6 = so_df[(so_df['creationdate'] >= '2014-03-01') & (so_df['creationdate'] <= '2014-10-31') & (so_df['ans_name'] == 'unutbu') & (so_df['score'] < 5)]
q7 = so_df[(so_df['score'].between(5, 10)) | (so_df['viewcount'] > 10000)]
q8 = so_df[so_df['ans_name'] != 'Scott Boston']

# Titanic Tasks
t1 = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) & (titanic_df['Age'].between(20, 30))]
t2 = titanic_df[titanic_df['Fare'] > 100]
t3 = titanic_df[(titanic_df['Survived'] == 1) & (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]
t4 = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]
t5 = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
t6 = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]
t7 = titanic_df[(titanic_df['Cabin'].notnull()) & (titanic_df['Fare'] > 200)]
t8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
t9 = titanic_df[titanic_df.duplicated('Ticket', keep=False) == False]
t10 = titanic_df[(titanic_df['Name'].str.contains('Miss')) & (titanic_df['Pclass'] == 1)]
