import requests
import json
from pprint import pprint


def GetMSStock():
    uh = requests.get('http://finance.google.com/finance/info?client=ig&q=MSFT')
    data = uh.content
    data = str(data.decode('utf-8'))
    data = data.replace('// [', '')
    data = data.replace("\n]\n", '')

    # print(data)
    print('Retrieved', len(data), 'characters')
    #data = data.decode("utf-8")

    js = json.loads(data)
    pprint(js)
    print('id', js['id'])
    return js
