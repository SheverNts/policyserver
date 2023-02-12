from setuptools import setup, find_packages
from codecs import open
from os import path
# from policyserver import config
#from dotenv import load_dotenv

#load_dotenv()

here = path.abspath(path.dirname(__file__))

__version__ = "0.0.1"

# Get the long description from the README file
with open(path.join(here, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()
packages = [
    'policyserver',
    'policyserver.commands',
    'policyserver.core'
]

setup(
    name='policyserver',
    version=__version__,
    packages=packages,
    include_package_data=True,
    author='Shever Natsai',
    # install_requires=install_requires,
    # dependency_links=dependency_links,
    author_email='shevernts@gmail.com'
)