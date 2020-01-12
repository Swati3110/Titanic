import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic=pd.read_csv('titanic.csv')


#df=pd.DataFrame(titanic.select_dtypes(exclude=['object']))

#a=titanic.groupby(['Sex','Survived'])['Age'].mean()
#print(a)

#c=titanic.pivot_table(index=['Sex','Survived'],values='Age',aggfunc='mean')
#print(c)

d=titanic.pivot_table(index=['Sex','Survived'],values='Age',aggfunc='mean').reset_index()
#print(d)

# e=pd.DataFrame(titanic.pivot_table(index=['Sex'],columns=['Survived'],values='Age',aggfunc='mean'))
# print(e)
d.rename(columns={"Age":"Avg_age"},inplace=True)

# titanic_new=titanic.merge(d,on=['Sex','Survived'],how='inner').mean()
# print(titanic_new)
# unique=titanic['Fare'].nunique()
# print(unique)

#unique=titanic['Fare'].qcut(5)
# unique=pd.qcut(titanic['Fare'], q=5)
# print(unique)





