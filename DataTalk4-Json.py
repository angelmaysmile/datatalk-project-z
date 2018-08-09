# HOW TO HANDLE JSON DATA
import pandas as pd
import json

# Open json data
with open("champion_info_2.json", "r+") as f:
    json_data = json.load(f)
champion = pd.DataFrame(json_data)
champion.reset_index(inplace=True)
champion.rename(columns={"index": "name"}, inplace=True)
champion.head()

# Get all separate keys of the json data
columns = []
def get_keys(dictionary):
    global columns
    for k, v in dictionary.items():
        if isinstance(v, dict):
            get_keys(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    get_keys(item)
        else:
            columns.append(k)

# Find all values of a key
def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result

# Create new columns with the keys
for item in champion.data.tolist():
    get_keys(item)
key_list = set(columns)
for key in key_list:
    champion[key] = ''

champion.head()

# Find value and fill the data frame
for i in range(champion.shape[0]):
    for key in key_list:
        found_value = list(find(key, champion.data[i]))
        champion[key][i] = found_value[0] if len(found_value) > 0 else ''

# Final result
champion.head()

