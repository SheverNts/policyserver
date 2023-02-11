from setuptools import setup, find_packages
from codecs import open
from os import path
from policyserver import config
#from dotenv import load_dotenv

#load_dotenv()

here = path.abspath(path.dirname(__file__))

__version__ = config.VERSION

# Get the long description from the README file
with open(path.join(here, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()
packages = [
    'policyserver',
    'policyserver.commands',
    'policyserver.core'
]
# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '')
                    for x in all_reqs if x.startswith('git+')]

setup(
    name='policyserver',
    version=__version__,
    packages=packages,
    include_package_data=True,
    author='Shever',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='shevernts@gmail.com',
    entry_points={
        'console_scripts': [
            'policyserver = policyserver.cli:main',
        ]}
)