import http.client
import json

def getRepositories(org):
    headers = {"User-Agent": "python-github-api"}
    conn = http.client.HTTPSConnection("api.github.com")
    conn.request("GET", f'/search/repositories?q=org:{org}&sort=updated&order=desc', '', headers)

    response = conn.getresponse()
    data     = response.read()
    return json.loads(data.decode("utf-8")) 

def filterRepositoriesData(data):
    reposList = []
    for repo in data["items"]:
        reposList.append({
            "name": repo["name"],
            "description": repo["description"],
            "url": repo["html_url"],
            "language": repo["language"] or "",
        })

    return reposList

repos = []
try:
    data  = getRepositories("AlexisReyes")
    repos = filterRepositoriesData(data)
except Exception as e:
    raise e
finally:
    print(json.dumps(repos))
