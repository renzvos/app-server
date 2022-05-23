import re
import time
import subprocess

def startup_commands():
  print("Starting Apache")
  p = subprocess.Popen(['service apache2 start'], stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()  
  p_status = p.wait()
  print(output)
  #print("Waiting")
  #time.sleep(10)
  #print("Starting MYSQL")
  #p = subprocess.Popen(['service mysql start'], stdout=subprocess.PIPE, shell=True)
  #(output, err) = p.communicate()  
  #p_status = p.wait()
  #print(output)

  
  print("Enableing Module Headers")
  p = subprocess.Popen(['a2enmod headers'], stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()  
  p_status = p.wait()
  print(output)


def certbot_run(vhosted):
  urls = ""
  for project in vhosted:
    urls = urls + project['url'] + ',' + project['url-alias'] + ','
  urls = urls[:-1]
  print("Starting Certbot")
  cmd = "certbot -n -m nazir.arshad7@gmail.com -d "+ urls +" --agree-tos --apache"
  print(cmd)
  p = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()  
  p_status = p.wait()
  print(output)


def projectname_regex(item):
    r = re.compile('config_projects_(.*?)_enabled')
    m = r.search(item)
    if m:
        projectname = m.group(1)
        return projectname
    else:
        return False


def findProjectIndex(name, list):
  for id in range(len(list)):
    if list[id]["name"] == name:
      return id