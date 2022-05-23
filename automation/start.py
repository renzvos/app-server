import init
import support
from scripts import gitpull
import os

dev = False
config = {}
if dev:
    projectdestination = "C:\dev-server-host-temp\\"
    config["config_log_everysteps"]  = "false"
    config["config_projects_rex_prealpha_enabled"] = "true"
    config["config_projects_rex_prealpha_address_mode"] = "vhost"
    config["config_projects_rex_prealpha_address_url_name"] = "prealpha.rex.renzvos.com"
    config["config_projects_rex_prealpha_address_url_alias"] = "www.prealpha.rex.renzvos.com"
    config["config_projects_rex_prealpha_host_source"] = "github"
    config["config_projects_rex_prealpha_host_credentials_account"] = "Rexplanatory"
    config["config_projects_rex_prealpha_host_credentials_branch"] = "pre-alpha"
    config["config_projects_rex_prealpha_host_credentials_password"] = "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"
    config["config_projects_rex_prealpha_host_credentials_repo"] = "rex-server"
    config["config_projects_rex_prealpha_host_credentials_username"] = "arshad@email.com"
    config["config_projects_rex_prealpha_mysql_db_database"] = "rexdev"
    config["config_projects_rex_prealpha_mysql_db_host"] = "192.168.265.23"
    config["config_projects_rex_prealpha_mysql_db_password"] = "asas"
    config["config_projects_rex_prealpha_mysql_db_username"] = "rexuser"
else:
    projectdestination = "/var/www/html/"
    for item, value in os.environ.items():
        config[item] = value


if(config['config_log_everysteps'] == "true"):logall = True
else:logall = False


vhostlocation = r'/etc/apache2/sites-enabled/'

print("Hosting location is " + projectdestination)
print("Vhost locations is" + vhostlocation)
print("Environment Variables")
for item, value in config.items():
    print(" " + item + " : " + value)


support.startup_commands()
githubprojects , vhosted = init.main(config, projectdestination , vhostlocation, logall)
print("Initialisation Complete")
support.startup_commands()

while True:
    #pulling all
    gitpull.main(githubprojects,logall)




