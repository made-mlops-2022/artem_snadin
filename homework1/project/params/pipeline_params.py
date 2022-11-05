from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema

from .downloading_params import DownloadParams
from .splitting_params import SplittingParams
from .train_params import TrainParams
from .feature_params import FeatureParams


@dataclass()
class PipelineParams:
    input_data_path: str
    downloading_params: DownloadParams
    train_params: TrainParams
    splitting_params: SplittingParams
    feature_params: FeatureParams


PipelineParamsSchema = class_schema(PipelineParams)


def read_pipeline_params(path: str) -> PipelineParams:
    with open(path, "r") as input_stream:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
