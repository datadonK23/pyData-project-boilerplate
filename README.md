# pyData-project-boilerplate
Project structure for prototyping using PyData Stack

# $PROJECTNAME
$PROJECTDESCRIPTION

More informations in project briefing: `BRIEFING.md`


# Conda Environment
Rename environment name in yml, run `conda env create -f environment.yml` and `source activate $ENVNAME`


# App Entry Point
Start app with `python $PROJNAME/main.py` (or `cd` into `$PROJNAME/`-directory and run `python main.py`).

OR Change directory to `$PROJNAME/notebook`, run `jupyter notebook` and select a notebook.


# Project Structure
```bash
.
├── BRIEFING.md # project briefing
├── docs # documentation & research content
│   └── info.md
├── environment.yml # conda environment
├── LICENSE
├── project #TODO rename $PROJNAME
│   ├── data
│   │   ├── __init__.py
│   │   └── REFS.md
│   ├── __init__.py
│   ├── main.py # entry point
│   ├── model.py
│   ├── models # persist models
│   │   └── __init__.py
│   ├── notebook
│   │   ├── 0_Cleaning.ipynb
│   │   ├── 1_Exploration.ipynb
│   │   ├── 2_Modeling.ipynb
│   │   ├── helpers
│   │   │   └── __init__.py
│   │   └── plots
│   │       └── __init__.py
│   └── test
│       ├── __init__.py
│       ├── test_main.py
│       └── test_model.py
├── README.md
├── RESULTS.md # project results
└── TODO.md
```

# License
Apache License Version 2.0
