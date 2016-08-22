from subprocess import call
import os

project = raw_input("Name of project (Assuming desired path is '..'): ")
pwd = os.environ['PWD']
path = pwd + "/../" + project

reserved = ["bin", "build", "data", "dist", "docs", "NAME", 
        "projectname.egg-info", "tests", "venv"]
if not project.isalnum() or os.path.exists(path) or project in str(reserved): #any(project in s for s in reserved):
    print "Not a valid name"
    exit()

zipname = "master.zip"
reponame = "python_skeleton"
repo = "https://github.com/poeks/"+ reponame +"/archive/" + zipname

print "Making new project " + project + " at " + path

f = open(zipname, "w")
call(["curl", "-L", repo], stdout=f)
call(["unzip", zipname])

call(["mv", reponame + "-master", project])
call(["mv", project, path])

call(["rm", zipname])
call(["rm", reponame + "-master", "-rf"])
