# What's This?
This is a project skeleton for python projects. It includes a cement command line interface.

# Installation

* Install python, pip, virtualenv
* Run:
~~~~
virtualenv venv
source venv/bin/activate
python setup.py install
~~~~

# Usage

`bin/create_project # creates new project`

* Then from newly made directory (`../projectname`):

~~~~
bin/cli --h # show all options
bin/cli thing -f foo --debug # run example option with parameter foo
~~~~

* Write your code as usual in `../projectname`!
