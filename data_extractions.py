#%%
import pandas as pd
import requests

#%%
singles_data_json = requests.get(r'https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/15694.json').json()

singles_data = pd.json_normalize(singles_data_json, 'Level2')
singles_data.rename(columns={'level_1': 'Age Range', 'level_2': 'Gender', 'value': 'Proportion'}, inplace=True)
singles_data['Last Updated'] = pd.json_normalize(singles_data_json)['DataLastUpdated'][0]
singles_data

#%%
marital_status_json = requests.get(r'https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/12082.json').json()

marital_status = pd.json_normalize(marital_status_json, 'Level2')
marital_status.rename(columns={'value': 'Number of Individual'}, inplace=True)
marital_status['Last Updated'] = pd.json_normalize(marital_status_json)['DataLastUpdated'][0]

#%%
births_and_fertility_data_json = requests.get(r'https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/13273.json').json()

births_and_fertility_data_age_range = pd.json_normalize(births_and_fertility_data_json, 'Level2a')
births_and_fertility_data_age_range.rename(columns={'level_2': 'Age Range', 'value': 'Total Fertility Rate'}, inplace=True)
births_and_fertility_data_age_range['Last Updated'] = pd.json_normalize(births_and_fertility_data_json)['DataLastUpdated'][0]

births_and_fertility_data_race = pd.json_normalize(births_and_fertility_data_json, 'Level2b')
births_and_fertility_data_race.rename(columns={'level_2': 'Gender', 'value': 'Total Fertility Rate'}, inplace=True)
births_and_fertility_data_race['Last Updated'] = pd.json_normalize(births_and_fertility_data_json)['DataLastUpdated'][0]

#%%
cpf_contribution_data_json = requests.get(r'https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/15257.json').json()
cpf_contribution_data = pd.json_normalize(cpf_contribution_data_json, 'Level3')
cpf_contribution_data.rename(columns={'value': 'Value in Millions'}, inplace=True)
cpf_contribution_data['Last Updated'] = pd.json_normalize(cpf_contribution_data_json)['DataLastUpdated'][0]
