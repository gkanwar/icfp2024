import json
import requests

from ir import *

headers = {
    'User-Agent': 'Team-IDKJava',
}
with open('.auth.json', 'r') as f:
    headers.update(json.load(f))
print(headers)
