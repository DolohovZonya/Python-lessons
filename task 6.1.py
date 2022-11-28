import pandas as pd
from collections import Counter

df = pd.read_excel('input_6_1.xlsx')
#print(df.head(3))
df_mask = (df['Цена'] == df['Цена'].max())
print(df[df_mask])
df['Цена'].max()
df_by_year = df.groupby(['Год покупки'])['Наименование'].count()   
print(df_by_year)
df_top1 = (df_by_year == df_by_year.max())
print(df_by_year[df_top1])
df_top3 = df.groupby(['Издатель'])['Наименование'].count().sort_values(ascending = False).head(3)
print(df_top3)
def min_playser(players):
    s = players.split('-')[0]
    return s
def max_playser(players):
    s = players.split('-')[1]
    return s
df['min_Число игроков'] = df['Число игроков'].apply(min_playser)
df['max_Число игроков'] = df['Число игроков'].apply(max_playser)         
df['range'] = df.apply(lambda x: range(int(x['min_Число игроков']), int(x['max_Число игроков']) + 1), axis = 1)
play = df['range'].explode()
play = play.value_counts()
print(play)
df['max_Число игроков'] = df['max_Число игроков'].astype(int)
df_med = df.groupby(['Жанр'])['max_Число игроков'].median()
print(df_med)
df_med = df.groupby(['Жанр'])['max_Число игроков'].mean() #check
print(df_med)
df['Coefficient'] = df.apply(lambda x: x['Реиграбельность'] - x['Сложность'], axis = 1)
df = df.sort_values(by = ['Coefficient'], ascending = False)
mech = df['Механики'].str.lower()
mech = mech.str.get_dummies(', ')
print(mech.head(1))
mech_sum = mech.apply(sum)
sum_all = mech_sum.sum()
print(sum_all)
mech_sum = mech_sum/sum_all*100
print(mech_sum)
