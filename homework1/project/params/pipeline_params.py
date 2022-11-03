from dataclasses import dataclass
from .downloading_params import DownloadParams
from .train_params import TrainParams
from .splitting_params import SplittingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class PipelineParams:
    input_data_path: str
    downloading_params: DownloadParams
    train_params: TrainParams
    splitting_params: SplittingParams


PipelineParamsSchema = class_schema(PipelineParams)


def read_pipeline_params(path: str) -> PipelineParams:
    with open(path, "r") as input_stream:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))



