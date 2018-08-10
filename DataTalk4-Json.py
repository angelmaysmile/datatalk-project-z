# HOW TO HANDLE JSON DATA
import pandas as pd
import json
import parse_json

# Open json data
with open("Leagues of Legends/champion_info_2.json", "r+") as f:
    json_data = json.load(f)
champion = pd.DataFrame(json_data)
champion.reset_index(inplace=True)
champion.rename(columns={"index": "name"}, inplace=True)
champion.head()

# Convert the json data to DataFrame
first_row_data = champion.data[0]
champ_data = pd.DataFrame(first_row_data)
for i in range(1, champion.shape[0]):
    champ_data = champ_data.append(pd.DataFrame(champion.data[i]))
champ_data = pd.DataFrame(champ_data.groupby(['title', 'id', 'name', 'key'])['tags'].apply(lambda x: "%s" % ', '.join(x)))
champ_data.reset_index(inplace=True)
champ_merge = pd.merge(champion, champ_data, how="left", on="name")
print(champion.head())

# General method to parse json and add data to the dataframe
champion = parse_json.parse_json(champion, 'data')
print(champion.head()_

