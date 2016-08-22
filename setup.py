try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jen Oslislo',
    'url': 'http://github.com/poeks/project',
    'download_url': 'http://github.com/poeks/project',
    'author_email': 'oslisloth@gmail.com',
    'version': '0.1',
    'license': 'Apache 2.0',
    'install_requires': ['nose', 'cement'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
