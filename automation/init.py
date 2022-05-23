from apps.githubcommands import githubcommands
from apps import vhostdata
import support


def main( config,projectdestination, vhostlocation , logall):
    githubprojects = []
    vhosted = []
    print("Making Projects Ready")
    for item, value in config.items():
        if(logall) : print("Item is " + item)
        if(logall) : print("Value is " + value)
        if item.startswith("config_projects_") and item.endswith("_enabled") and value == "true":
            if(logall) : print("Found a project enabled : " + item)
            projectname = support.projectname_regex(item)
            if projectname != False:
                print("Initiating Project - " + projectname)
                envaddr = 'config_projects_' + projectname
                if config[ envaddr + '_host_source'] == "github":
                    username = config[ envaddr + "_host_credentials_username"]
                    password = config[ envaddr + "_host_credentials_password"]
                    account = config[ envaddr + "_host_credentials_account"]
                    rep = config[envaddr + "_host_credentials_repo"]
                    branch = config[envaddr + "_host_credentials_branch"]
                    destination  = projectdestination + projectname + "/"
                    print("Project Code Source : Github - " + account + " as user " + username)
                    print("Downloading " + branch + " branch")
                    githubcommands.clone_password(username,password,account,rep,destination,branch=branch)
                    sha = githubcommands.windows_fetchsha(account,rep,username,password,branch)
                    githubprojects.append({"name": projectname , "username":username , "password" : password , "account" : account , "repo" : rep , "branch": branch , "destination" :destination , "final-sha" : sha})

                if config[ envaddr + "_address_mode"] == "vhost":
                    url = config[ envaddr  +  "_address_url_name"] 
                    url_alias =  config[  envaddr  +  "_address_url_alias"] 
                    destination  = projectdestination + projectname + "/"
                    data = vhostdata.vhostdata(url,url_alias,destination)
                    with open(vhostlocation + 'rex.conf', 'w') as f:
                        f.write(data)
                    vhosted.append({"name" : projectname , "url" : url , "url-alias" : url_alias})
            else:
                print("Cannot parse project name")    

    #support.certbot_run(vhosted)
    return githubprojects,vhosted
