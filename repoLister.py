import json
import urllib

user = raw_input() # Get the user that repo list is wanted from

print "Downloading user info for user '"+user+"'"
urllib.urlretrieve("https://api.github.com/users/"+user, "userdata.json") # download a json file of their userinformation

print "User info downloaded.\nDownloading user repo list for user '"+user+"'"
urllib.urlretrieve("https://api.github.com/users/"+user+"/repos?page=1&per_page=10000", "repos.json") # download a json file of their repos

with open('repos.json') as data_file:
    githubRepoData = json.load(data_file)
with open('userdata.json') as data_file:
    githubUserData = json.load(data_file)

try:
    repoAmount = int(githubUserData["public_repos"])-1
except ValueError:
    print("Error: could not get public repos index as integer")
index = 0

print "\nRepositories:"

for _ in range(repoAmount+1):
    print index+1,"\t",githubRepoData[index]["name"]
    repoAmount -= 1
    index += 1
