import requests
import json



fs = open('data.json', 'r')
JSON = json.load(fs)
version = JSON['version']
# =========================================================================== #
response = requests.get('https://raw.githubusercontent.com/WHITE71wolf/Minecraft-Generator-Skins/main/data.json').text
j = json.loads(response)
new_version = j['version']
new_url = j['url']
if new_version != version:
    res = requests.get(new_url)
    with open('updater.pyc', 'wb') as file:
        for data in res.iter_content(chunk_size=8192):
            file.write(data)





