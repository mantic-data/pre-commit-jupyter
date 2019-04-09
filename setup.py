import sys
from setuptools import find_packages
from setuptools import setup

install_requires = ['isort>=4.1.1,<5']
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='pre_commit_python_nbconvert',

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'python-nbconvert = pre_commit_hook.nbconvert:main',
        ],
    },
)
