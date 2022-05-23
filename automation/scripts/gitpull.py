from apps.githubcommands import githubcommands
import time
import support

def main(githubprojects,logall):
    for project in githubprojects:
        try:
            sha = githubcommands.windows_fetchsha(project["account"],project["repo"],project["username"],project["password"],project["branch"])
            if(logall): print("Online " + sha)
            if(logall): print("Local " + project["final-sha"])
            if sha == project['final-sha']:
                if(logall): print("No change")
            else:
                print("Pulling" + project["name"])
                githubcommands.pull(project["destination"])
                id = support.findProjectIndex(project["name"],githubprojects)
                githubprojects[id]['final-sha'] = sha
        except Exception as e:
            print("Failed ")
            print(e)
        time.sleep(5)
