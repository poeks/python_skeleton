from subprocess import call
import os

project = raw_input("Name of project (Assuming desired path is '..'): ")
if not project.isalnum():
    print "Not a valid name"
    exit()

zipname = "master.zip"
reponame = "python_skeleton"
repo = "https://github.com/poeks/"+ reponame +"/archive/" + zipname
home = os.environ['PWD']
path = home + "/../" + project

print "Making new project " + project + " at " + path
call(["mkdir", path])
os.chdir(path)

f = open(zipname, "w")
call(["curl", "-L", repo], stdout=f)
call(["unzip", zipname])
call(["mv", reponame + "/*", path])

