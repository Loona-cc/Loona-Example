import json
import imp
from flask import Flask
from flask import *

data = {}
data['Config'] = []
data['Config'].append({
'manifest': 'v1',
'version': '1.0',
'file': 'testmodule.py',
'url': 'https://github.com/Loona-cc/Loona-Module'
})
with open('manifest.json', 'w+') as of:
    json.dump(data, of)
