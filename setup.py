from setuptools import find_packages
from setuptools import setup

install_requires = []  # ['isort>=4.1.1,<5']

setup(
    name='pre_commit_jupyter',
    url='https://github.com/mantic-data/pre-commit-jupyter',
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pre-commit-jupyter = entry:main',
        ],
    },
)
