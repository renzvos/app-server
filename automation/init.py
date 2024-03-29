from apps.githubcommands import githubcommands
from apps import vhostdata
from apps.arsenal import Arsenal
from apps.arsenal.connection import connection

import support


arsenalc = Arsenal()

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
                    destination  = projectdestination + projectname
                    print("Project Code Source : Github - " + account + " as user " + username)
                    print("Downloading " + branch + " branch")
                    githubcommands.clone_password(username,password,account,rep,destination,branch=branch)
                    sha = githubcommands.windows_fetchsha(account,rep,username,password,branch)
                    print("CHOWNing")
                    support.Chown("www-data",destination)
                    print("Global safe adding")
                    githubcommands.GlobalAddSafe(destination)
                    githubprojects.append({"name": projectname , "username":username , "password" : password , "account" : account , "repo" : rep , "branch": branch , "destination" :destination , "final-sha" : sha})
  
                apachevars = open('/etc/apache2/envvars', 'a')
                apachevars.write('\n')
                if envaddr + "_mysql_db_database" in config:
                    apachevars.write('export ' + envaddr + "_mysql_db_database=" + config[envaddr + "_mysql_db_database"] + "\n")
                else:print("Database Name not found")
                if envaddr + "_mysql_db_host" in config:
                    apachevars.write('export ' + envaddr + "_mysql_db_host=" + config[envaddr + "_mysql_db_host"]+ "\n")
                else:print("Database-Host Name not found")
                if envaddr + "_mysql_db_password" in config:
                    apachevars.write('export ' + envaddr + "_mysql_db_password=" + config[envaddr + "_mysql_db_password"]+ "\n")
                else:print("Database Password not found")               
                if envaddr + "_mysql_db_username" in config:
                    apachevars.write('export ' + envaddr + "_mysql_db_username=" + config[envaddr + "_mysql_db_username"]+ "\n")
                else:print("Database Username not found")
                apachevars.close()

                if config[ envaddr + "_address_mode"] == "vhost":
                    url = config[ envaddr  +  "_address_url_name"] 
                    url_alias =  config[  envaddr  +  "_address_url_alias"] 
                    destination  = projectdestination + projectname + "/"
                    if config[envaddr + "_ssl"] == "true":
                        certlocation = None
                        keylocation = None
                        chainfilelocation  = None
                        if config[envaddr + "_ssl_certificate_source"] == "dropbox":
                            cloud_dir = config[envaddr + '_ssl_certificate_source_path']
                            access = config[envaddr + '_ssl_certificate_source_access']
                            certlocation = "/volume/certificates/" + projectname + "/"
                            conn = connection(projectname + "-ssl-cert",certlocation)
                            conn.dropbox(access,cloud_dir)
                            arsenalc.Download(conn,projectname + ".pem")
                            print("Downloaded Certificate")
                            certlocation = certlocation + projectname + ".pem"
                        if config[envaddr + "_ssl_key_source"] == "dropbox":
                            cloud_dir = config[envaddr + '_ssl_key_source_path']
                            access = config[envaddr + '_ssl_key_source_access']
                            keylocation = "/volume/certificates/" + projectname + "/"
                            conn = connection(projectname + "ssl-key",keylocation)
                            conn.dropbox(access,cloud_dir)
                            arsenalc.Download(conn,projectname + ".key")
                            print("Downloaded Key")
                            keylocation = keylocation + projectname + ".key"
                        if envaddr + "_ssl_chainfile_source" in config:
                            if config[envaddr + "_ssl_chainfile_source"] == "dropbox":
                                cloud_dir = config[envaddr + '_ssl_chainfile_source_path']
                                access = config[envaddr + '_ssl_chainfile_source_access']
                                chainfilelocation = "/volume/certificates/" + projectname + "/"
                                conn = connection(projectname + "ssl-chainfile",chainfilelocation)
                                conn.dropbox(access,cloud_dir)
                                arsenalc.Download(conn,projectname + ".pem")
                                print("Downloaded Chain File")
                                chainfilelocation = chainfilelocation + projectname + ".pem"
                                data = vhostdata.vhostssl(url,url_alias,destination,certlocation,keylocation,chainfilelocation)
                                with open(vhostlocation + projectname +  '-ssl.conf', 'w') as f:
                                    f.write(data)
                                    f.close()
                                vhosted.append({"name" : projectname , "url" : url , "url-alias" : url_alias , "ssl" : True})
                        else:
                            data = vhostdata.vhostssl(url,url_alias,destination,certlocation,keylocation)
                            with open(vhostlocation + projectname +  '-ssl.conf', 'w') as f:
                                f.write(data)
                                f.close()
                            vhosted.append({"name" : projectname , "url" : url , "url-alias" : url_alias , "ssl" : True})
                        
                    else:
                        data = vhostdata.vhostdata(url,url_alias,destination)
                        with open(vhostlocation + projectname +  '.conf', 'w') as f:
                            f.write(data)
                            f.close()
                        vhosted.append({"name" : projectname , "url" : url , "url-alias" : url_alias , "ssl" : False})






            else:
                print("Cannot parse project name")    

    #support.certbot_run(vhosted)
    return githubprojects,vhosted
