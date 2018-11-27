from pandas.io.json import json_normalize
import json
import os
import re

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

file = 'infomoney'
path = '/home/lin/Documents/tweepy/{}.json'.format(file)
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
    df = json_normalize(flat)
    df.drop(df.columns.difference(['created_at', 'id', 'user_name', 'user_followers_count', 'favorite_count', 'retweet_count', 'full_text']), 1, inplace=True)

    # Escrever em CSV
    csv = '/home/lin/Documents/tweepy/{}.csv'.format(file)
    file_exists = os.path.isfile(csv)
    with open(csv, 'a') as f:
        if not file_exists:
            df.to_csv(f, sep=';', index=False)
        else:
            df.to_csv(f, sep=';', header=False, index=False)

os.remove('temp.json')
