import pandas as pd


pd.set_option('display.max_columns', 8)

general = pd.read_csv('C:/Haritosh/Programming/Python/02 JetBrainsAcademy/03 Introductory Machine Learning in Python/Medium/Data Analysis For Hospitals/project/test/general.csv', encoding='utf-8')
prenatal = pd.read_csv('C:/Haritosh/Programming/Python/02 JetBrainsAcademy/03 Introductory Machine Learning in Python/Medium/Data Analysis For Hospitals/project/test/prenatal.csv', encoding='utf-8')
sports = pd.read_csv('C:/Haritosh/Programming/Python/02 JetBrainsAcademy/03 Introductory Machine Learning in Python/Medium/Data Analysis For Hospitals/project/test/sports.csv', encoding='utf-8')

general.drop(columns='Unnamed: 0', inplace=True)
prenatal.drop(columns='Unnamed: 0', inplace=True)
sports.drop(columns='Unnamed: 0', inplace=True)

prenatal.rename(columns={'HOSPITAL':'hospital', 'Sex':'gender'}, inplace=True)
sports.rename(columns={'Hospital':'hospital', 'Male/female':'gender'}, inplace=True)

df = pd.concat([general, prenatal, sports], ignore_index=True)
# ignore_index=True makes it so that the indexes are all from 0, 1, 2, 3, ... since otherwise, the indexes are unordered
print(df.sample(n=20, random_state=30))
