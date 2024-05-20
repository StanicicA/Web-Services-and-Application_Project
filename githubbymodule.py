from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

repo = g.get_repo("andrewbeattycourseware/aprivateone")

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

newContents = contentOfFile + " more stuff 2 \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)