import requests
import json
from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

apikey='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'

#apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)


with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)