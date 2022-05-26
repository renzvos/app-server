from platform import platform
import subprocess
import urllib.parse
import sys
import os
sys.path.append(os.path.dirname(__file__))
import git
from pydriller import Repository
from datetime import datetime, timezone, timedelta
from git import Repo

platform = sys.platform


def setuser(name,email,path):
   if platform == "linux":
      p = subprocess.Popen(['cd ' + path + ' && git config --global user.email "' + email + '"'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
      p = subprocess.Popen(['cd ' + path + ' && git config --global user.name "' + name + '"'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
   else:
      print("Not developed for " + platform)

def clone_link(link , destination):
   if platform == "linux":
      username = urllib.parse.quote(username)
      password = urllib.parse.quote(password)
      account = urllib.parse.quote(account)
      rep = urllib.parse.quote(rep)
      p = subprocess.Popen(['git clone ' + link + ' ' + destination], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
      print("Processing")

      if(destination == ""):
         path = rep
      else:
         path = destination + '/' + rep

      if(os.path.exists(path)):
         print("Repository Cloned Successfully")
         return True
      else:
         print("Repository Cloning Failed")
         return False
   else:
      print("Not developed for " + platform)


def clone_password(username, password , account , rep , destination , branch=None):
   if platform == "linux":   
      username = urllib.parse.quote(username)
      password = urllib.parse.quote(password)
      account = urllib.parse.quote(account)
      rep = urllib.parse.quote(rep)
      if branch == None: p = subprocess.Popen(['git clone https://' + username+ ':' + password + '@github.com/' + account + '/'+ rep + '.git ' + destination], stdout=subprocess.PIPE, shell=True)
      else :  p = subprocess.Popen(['git clone https://' + username+ ':' + password + '@github.com/' + account + '/'+ rep + '.git --branch ' + branch + ' --single-branch ' + destination], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()

      if(destination == ""):
         path = rep
      else:
         path = destination + '/' + rep

      if(os.path.exists(path)):
         print("Repository Cloned Successfully")
         return True
      else:
         print("Repository Cloning Failed")
         return False
   elif platform == "win32":
      username = urllib.parse.quote(username)
      password = urllib.parse.quote(password)
      account = urllib.parse.quote(account)
      rep = urllib.parse.quote(rep)
      if branch == None: p = subprocess.Popen(['git','clone','https://' + username+ ':' + password + '@github.com/' + account + '/'+ rep + '.git ',destination], stdout=subprocess.PIPE, shell=True)
      else :  p = subprocess.Popen(['git','clone','https://' + username+ ':' + password + '@github.com/' + account + '/'+ rep + '.git','--branch',branch,'--single-branch',destination], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
      print(output)

def push(path,message):
   if platform == "linux":   
      p = subprocess.Popen(['cd ' + path + ' && git add .'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()

      p = subprocess.Popen(['cd ' + path + ' && git commit -m "'+ message +'"'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()

      p = subprocess.Popen(['cd ' + path + ' && git push'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
   else:
      print("Not developed for " + platform)

def pull(path):
   if platform == "linux":   
      p = subprocess.Popen(['cd ' + path + ' && git pull'], stdout=subprocess.PIPE, shell=True)
      (output, err) = p.communicate()  
      p_status = p.wait()
      print(output)
   elif platform == "win32":
      g = git.cmd.Git(path)
      g.pull()


def windows_subtree_add(path,account,repo,destination,username,password):
   print("Windows Git Tree Add")
   command = "cd " + path + " && git subtree add --prefix " + destination + " https://" + username + ':' + password + '@github.com/' + account + '/'+ repo + '.git' + " main --squash"
   os.system('cmd /c "' + command + '"')
   print("Restart the Program")

def windows_subtree_pull(path,account,repo,destination,username,password):
   print("Windows Git Tree Pull")
   command = "cd " + path + " && git subtree pull --prefix " + destination + " https://" + username + ':' + password + '@github.com/' + account + '/'+ repo + '.git' + " main --squash"
   os.system('cmd /c "' + command + '"')
   print("Restart the Program")


def windows_subtree_push(path,account,repo,destination,username,password):
   print("Windows Git Tree Pushing " + repo)
   command = "cd " + path + " && git subtree push --prefix=" + destination + " https://" + username + ':' + password + '@github.com/' + account + '/'+ repo + '.git' + " main"
   os.system('cmd /c "' + command + '"')
   print("Restart the Program")

def windows_fetchsha(account,repo,username,password,branch=None):
   username = urllib.parse.quote(username)
   password = urllib.parse.quote(password)
   account = urllib.parse.quote(account)
   rep = urllib.parse.quote(repo)
   if branch == None:command = "git ls-remote https://"+username+":"+password+"@github.com/"+account+"/"+repo+".git HEAD"
   else: command = "git ls-remote https://"+username+":"+password+"@github.com/"+account+"/"+repo+".git refs/heads/" + branch
   #print(command)
   result = subprocess.check_output(command, shell=True)
   result =  result.decode()
   result = result.split("\t")[0]
   return result


def stagedfiles(path, filterdir=None):
    print("Path is " + path)
    if filterdir == None:
       filterdir = path
    uncommittedFiles = []
    repo = git.Repo(path)
    lastCommit = repo.head.commit.committed_date
    files = os.listdir(path)

    for root, dirs, files in os.walk(filterdir, topdown = True):
       for name in files:
         filepath = os.path.join(root, name)
         #print(filepath)
         if os.path.getmtime(filepath) > lastCommit:
               #print("Uncommited BRo" + str(filepath))
               uncommittedFiles.append(filepath)
       for name in dirs:
         #print(os.path.join(root, name))
         pass
       
    #print(len(uncommittedFiles))
    return uncommittedFiles

def fileschangedafter(date,path): 
   files = []
   date = datetime(date.year,date.month,date.day,hour=date.hour,minute=date.minute,second=date.second,tzinfo=timezone.utc)

   for commit in Repository(path).traverse_commits():

      if date < commit.author_date:
         #print(commit.msg)
         for file in commit.modified_files:
              files.append(file)
               
   return files

def SubtreeChanged(path,subtree,date):

   #print("SubtreeChanged " + path + " " + subtree)
   #print(date)
   staged = stagedfiles(path,filterdir=subtree)
   files = fileschangedafter(date,path)
   filepaths = []
   for file in files:
      if file.old_path != None:
         filepaths.append(file.old_path)
      if file.new_path != None:
         filepaths.append(file.new_path)

   subtree = subtree.split(os.sep)
   #print(subtree)
   includedfiles = 0
   for modpath in filepaths:
      #print("Checking the url " + modpath)
      modpathsplit = modpath.split(os.sep)
      for i in range(len(subtree)):
            #print("Checking folder " + subtree[i] + " and " + modpathsplit[i])
            if subtree[i] != modpathsplit[i]:
                  #print(modpath + "   is not included")
                  break
      else:
            #print(modpath + "  is included")
            includedfiles = includedfiles + 1

   #print(str(len(staged)) + " Staged")
   #print(str(includedfiles) + "Commited wating to pull to subtrees")
   if len(staged) + includedfiles ==  0:
       return "No",0,0       
   else:
       return "Yes",len(staged),includedfiles         


def AddAll_Commit(message,username):
   repo = Repo.init()
   repo.git.add('--all')  
   try:
      repo.git.commit('-m', message, author=username)
      return True
   except git.exc.GitCommandError as e:
      print(e)
      return False


