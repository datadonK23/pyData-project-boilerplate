# pyData-project-boilerplate
Project structure for prototyping using PyData Stack

# $PROJECTNAME
$PROJECTDESCRIPTION

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Rename environment name in yml, run `conda env create -f environment.yml` and `source activate $ENVNAME`

# Project Structure
* `README.md`
* `BRIEFING.md` _(project briefing)_
* `TODO.md`
* `environment.yml`
* `project/` _#TODO rename_
    * `__init__.py`
    * `main.py` _(entry point)_
    * `model.py`
    * `test/` _(test directory)_
        * `__init__.py`
        * `test_main.py`
        * `test_model.py`
    * `notebook/` _(notebooks for exploration & model development)_
        * `1_exploration.ipynb`
        * `helpers/`
            * `__init__.py`
    * `data/` _(data directory)_
        * `REFS.md`
* `docs/` _(documentation & research content)_
    * `research_docs`
* `LICENSE`

# License
Apache License Version 2.0
