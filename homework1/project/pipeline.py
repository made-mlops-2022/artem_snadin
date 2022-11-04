import json
import logging.config
import os
import sys
from pathlib import Path

import click
import pandas as pd
from params import read_pipeline_params

from data import download_data, read_data, split_train_val_data

from local_configs import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger("file_logger")


def train_pipeline(config_path: str):
    try:
        pipeline_params = read_pipeline_params(config_path)
    except FileNotFoundError:
        logger.error(f"config file {config_path} not found")
        return
    logger.info(f"read pipeline params from {config_path}")
    return run_train_pipeline(pipeline_params)


def run_train_pipeline(pipeline_params):
    downloading_params = pipeline_params.downloading_params
    if downloading_params:
        os.makedirs(downloading_params.output_folder, exist_ok=True)
        output_path = os.path.join(downloading_params.output_folder, downloading_params.filename)
        if not os.path.exists(output_path):
            logger.info(f"download dataset from {downloading_params.storage} to {output_path}")
            download_data(
                downloading_params.storage,
                output_path)
    logger.info(f"start pipeline with params {pipeline_params}")
    data = read_data(pipeline_params.input_data_path)
    logger.info(f"data.shape is {data.shape}")
    print(data)


print("aaa")


@click.command(name="train_pipeline")
@click.argument("config_path")
def train_pipeline_start(config_path: str):
    print(f"read pipeline params from {config_path}")
    train_pipeline(config_path)


if __name__ == "__main__":
    train_pipeline_start()
