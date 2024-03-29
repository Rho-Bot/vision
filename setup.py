from setuptools import setup, find_packages
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=find_packages('./include/.'),
    package_dir={'': 'include'},
    package_data={'': ['**/*.jpg']},
    include_package_data=True,)

setup(**setup_args)