import shutil
import os
from distutils.dir_util import copy_tree
import subprocess


phpconf = "config/php/php.ini"
apacheconf = "config/apache/apache2.conf"
vhosts = "config/vhost"
timelyact = "config/timelyact/config.json"
arsenal = "config/arsenal/config.json"

phplocation = r'/etc/php/7.2/apache2/php.ini'
apachelocation = r'/etc/apache2/'
vhostlocation = r'/etc/apache2/sites-enabled'
timelyactlocation = r'/usr/bin/timelyact/'
arsenallocation = r'/etc/arsenal/'

if os.path.exists(apachelocation):
    print("Apache Installation found")
    print('Changeing Apache Settings')
    if os.path.exists(apachelocation + "apache2.conf"):
        os.remove(apachelocation + "apache2.conf")
    shutil.copy(apacheconf,apachelocation)
    
    print('Deleting default Current Vhosts')
    for files in os.listdir(vhostlocation):
        path = os.path.join(vhostlocation, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    print('Copying all the vhost configuration')
    copy_tree(vhosts, vhostlocation)
    for files in os.listdir(vhostlocation):
        print("---" + str(files))
else:
    print("Apache Installation not found")



if os.path.exists(phplocation):
    print("PHP Installation found")
    print('Changeing Php Settings')
    if os.path.exists(phplocation + "php.ini"):
            os.remove(phplocation + "php.ini")
    shutil.copy(phpconf,phplocation)


else:
    print("PHP Config file not found")


if os.path.exists(timelyactlocation):
    print("RENZVOS Timelyact Installation found")
    print("Changing Timelyact Automation Configuration")
    if os.path.exists(timelyactlocation + "config.json"):
        os.remove(timelyactlocation + "config.json")
    shutil.copy(timelyact,timelyactlocation)
else:
    print("RENZVOS Timely Act Config file not found")


if os.path.exists(arsenallocation):
    print("RENZVOS Arsenal Installation Found")
    print('Changing Arsenal (RENZVOS TM) Backup Storage Configuration')
    if os.path.exists(arsenallocation + "config.json"):
        os.remove(arsenallocation + "config.json")
    shutil.copy(arsenal,arsenallocation)
else:
    print("RENZVOS Arsenal Backup Config file not found")


print("Restarting Apache")
p = subprocess.Popen(['sudo service apache2 restart'], stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()  
p_status = p.wait()

print("Restarting RENZVOS Timelyact")
p = subprocess.Popen(["sudo service renzvos-timelyact start"], stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()  
p_status = p.wait()