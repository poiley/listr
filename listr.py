import json, urllib, sys

class repoLister:
        user = ""
        githubRepoData = ""
        githubUserData = ""
        repoIndex = 0
        repositories = 0

        def downloadJSON(self,index):
            if index == 0:
                print "\nDownloading user info for user '"+self.user+"'"
                urllib.urlretrieve("https://api.github.com/users/"+self.user, "userdata.json") # download a json file of their userinformation
                print "User info downloaded."
            elif index == 1:
                print "\nDownloading user repo list for user '"+self.user+"'"
                urllib.urlretrieve("https://api.github.com/users/"+self.user+"/repos?page=1&per_page=10000", "repos.json") # download a json file of their repos
                print "Repo info downloaded."
            else:
                self.downloadJSON(0)
                self.downloadJSON(1)

        def readJSON(self,index):
            if index == 0:
                with open('repos.json') as data_file:
                    self.githubRepoData = json.load(data_file)
            elif index == 1:
                with open('userdata.json') as data_file:
                    self.githubUserData = json.load(data_file)
            else:
                self.readJSON(0)
                self.readJSON(1)

repository = repoLister()
if len(sys.argv) == 2:
    repository.user = sys.argv[1]
elif len(sys.args < 2):
    sys.exit("Error: No Args")
else:
    sys.exit("Error: Too many Args")

repository.downloadJSON(2)
repository.readJSON(2)

try:
    repository.repositories = int(repository.githubUserData["public_repos"]-1)
except ValueError:
    print("Error: could not get public repos index as integer")

print "\nRepositories:"

for _ in range(repository.repositories+1):
    print repository.repoIndex+1,"\t",repository.githubRepoData[repository.repoIndex]["name"]
    repository.repositories -= 1
    repository.repoIndex += 1
