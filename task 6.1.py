import pandas as pd
df = pd.read_excel("input.6.1.xlsx")
print(df.head(3))
df_mask = (df['Цена'] == df['Цена'].max())
print(df[df_mask])
df_by_year = df.groupby(['Год покупки'])['Наименование'].count()
df_top1 = (df_by_year == df_by_year.max())
print(df_by_year[df_top1])
df_top3 = df.groupby(['Издатель'])['Наименование']\
            .count()\
            .sort_values(ascending=False)\
            .head(3)
df['min Число игроков'] = df['Число игроков'].apply(min_player)
df['Макс число игроков'] = df['Макс число игроков'].astype(int)
df_med = df.groupby(['Жанр'])['Макс число игроков'].mean()
df['привлекательность'] = df.apply(lambda x: x['Реиграбельность'] - x['Сложность'], axis=1).sort_values()
                        
def min_player(string):
  string.split('-')
  return string[0]                       
