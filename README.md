# python_skeleton
Project skeleton for python projects. Includes cement command line interface.

# Installation

* Install python, pip, virtualenv
`virtualenv venv`
`source venv/bin/activate`
`python setup.py install`

# Usage
`bin/create_project # creates new project`

* Then from newly made directory (`../projectname`):
`bin/cli --h # show all options`
`bin/cli thing -f foo --debug # run example option with parameter foo`
