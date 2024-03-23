import json

with open('config.json', 'r') as f:
    config = json.load(f)

GOOGLE_API_KEY = config['google_api']['key']