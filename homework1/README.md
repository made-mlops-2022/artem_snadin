project
==============================

My simple ml project for MLOPS course.

Installation: 
~~~
pip install -r requirements.txt
~~~
Usage:
~~~
python project/pipeline.py configs/train_config_01.yaml
~~~

Test:
~~~
pytest tests/
~~~

Project Organization
------------

    ├── LICENSE
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data               <- Different datasets.
    │   │
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks with data analysis.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── tests              <- tests for project modules
    │ 
    ├── project            <- Source code for use in this project.
    │   │
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models to make
    │   │
    │   ├── local_configs  <- configs for logger
    │   │
    └── params             <- model parameters schemas


