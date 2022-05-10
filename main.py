import pandas as pd

covid_db = pd.read_csv('HIST_PAINEL_COVIDBR_2022_Parte1_09mai2022.csv',sep = ';')
pd.set_option('display.max_columns', None)
print(covid_db.head())
print(covid_db.shape)
print(covid_db.describe())
print(covid_db.isnull().sum())
print(covid_db.loc[pd.isnull(covid_db['estado'])])
covid_db = covid_db.dropna(subset=['estado', 'municipio'])
covid_db = covid_db.drop(['Recuperadosnovos', 'emAcompanhamentoNovos'], axis=1)

print(covid_db.isnull().sum())
print(covid_db.head())
print(covid_db.describe())
