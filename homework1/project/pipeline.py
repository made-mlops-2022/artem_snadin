import json
import os
import sys
from pathlib import Path
import click
import pandas as pd
from features import extract_target, build_transformer, make_features
from params import read_pipeline_params
from data import download_data, read_data, split_train_val_data
from models import ModelManager, Model
from local_configs import logger_config
import logging.config

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
    logger.info(f"dataset shape is {data.shape}")

    train_params = pipeline_params.train_params
    if train_params:
        logger.info(f"load models with {train_params}")
        try:
            ModelManager.load_models(train_params)
        except ValueError as ex:
            logger.error(f"model {ex} throw exception")
            return
    else:
        logger.error("training parameters not found")
        return

    logger.info(f"loaded models: {ModelManager.get_models()}")

    train_df, val_df = split_train_val_data(
        data, pipeline_params.splitting_params
    )

    val_target = extract_target(val_df, pipeline_params.feature_params)
    train_target = extract_target(train_df, pipeline_params.feature_params)
    train_df = train_df.drop(columns=pipeline_params.feature_params.target_col)
    val_df = val_df.drop(columns=pipeline_params.feature_params.target_col)

    logger.info(f"train dataframe shape is {train_df.shape}")
    logger.info(f"validation dataframe shape is {val_df.shape}")

    transformer = build_transformer(pipeline_params.feature_params)
    transformer.fit(train_df)
    train_features = make_features(transformer, train_df)

    logger.info(f"train features shape is {train_features.shape}")

    model = Model(ModelManager.get_model(train_params.model), train_params)
    model.train(train_features, train_target)
    model.create_inference_pipeline(transformer)
    predicts = model.predict(val_df)
    metrics = model.evaluate(predicts, val_target)
    logger.info(f"metrics: {metrics}")


@click.command(name="train_pipeline")
@click.argument("config_path")
def train_pipeline_start(config_path: str):
    train_pipeline(config_path)


if __name__ == "__main__":
    train_pipeline_start()
