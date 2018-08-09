import json
from collections import OrderedDict
with open("champion_info.json", "r+") as f:
    json_data = json.load(f)

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

with open("champion_info.csv", "w") as file:
    get_keys(json_data)
    to_write_dict = OrderedDict()
    key_list = list(set(columns))
    for item in key_list:
        to_write_dict[item] = list(find(item, json_data))
    file.write(','.join(to_write_dict.keys()))
    file.write("\n")
    max_length = max(list(map(lambda x: len(x), list(to_write_dict.values()))))
    key_length = len(to_write_dict.keys())
    count = 0
    while count < max_length:
        for k, v in to_write_dict.items():
            if len(v) == 1:
                file.write(str(v[0]))
            else:
                file.write(str(v[count]))
            file.write('') if key_list.index(k) == key_length - 1 else file.write(',')
        count += 1
        file.write("\n")
