from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="project",
    packages=find_packages(),
    version="1.0.0",
    description="My project for MLOps",
    author="Artem Snadin student of MADE 2022",
    entry_points={
        "console_scripts": [
            "model_train = project.train_pipeline:train_pipeline_start"
        ]
    },
    install_requires=required,
)