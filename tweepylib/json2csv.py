from pandas.io.json import json_normalize
import json
import os

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

path = '/home/lin/Documents/tweepy/b3.json'
f = open(path,"r")
contents = f.read()
contents = contents.split('\n')[:-1]

for row in range(0,len(contents)):
    q = open('temp.json', 'w')
    q.write(contents[row])
    q.close()

    with open('temp.json') as f:
        data = json.load(f)
        flat = flatten_json(data)

    print(json_normalize(flat))
    normalized_df = json_normalize(flat)

    # Escrever em CSV
    csv = '/home/lin/Documents/tweepy/b3.csv'
    file_exists = os.path.isfile(csv)
    with open(csv, 'a') as f:
        if not file_exists:
            normalized_df.to_csv(f, sep=';', index=False)
        else:
            normalized_df.to_csv(f, sep=';', header=False, index=False)

os.remove('temp.json')
