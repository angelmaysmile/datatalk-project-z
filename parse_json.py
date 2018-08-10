# A general method to convert json data to data frame (applies to muti-level json)

# Get all separate keys of the json data
columns = []
def get_keys(dictionary):
    global columns
    for k, v in dictionary.items():
        if isinstance(v, dict):
            get_keys(v)
        elif isinstance(v, list):
            columns.append(k)
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

# Function to parse json and add to dataframe
def parse_json(df, col_name):
    global columns
    # Create new columns with the keys
    for item in df[col_name].tolist():
        get_keys(item)
    key_list = set(columns)
    for key in key_list:
        df[key] = ''

    # Find value and fill the data frame
    for i in range(df.shape[0]):
        for key in key_list:
            found_value = list(find(key, df[col_name][i]))
            df[key][i] = found_value[0] if len(found_value) > 0 else ''
    return df