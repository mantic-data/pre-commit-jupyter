Pre-commit python jupyter notebook converter
===============================

This is a [pre-commit](https://github.com/pre-commit) hook that will convert your jupyter notebooks (*.ipynb) to python scripts and html files.

* [pre-commit](https://github.com/pre-commit)


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git://github.com/mantic-data/pre-commit-jupyter
      hooks:
      sha: master
      - id: python-nbconvert
       

Development: ``pip install -r requirements-dev.txt``

Testing: ``py.test --cov pre_commit_hook tests/``
