from typing import Optional

from dataclasses import dataclass
from download_params import DownloadParams
from train_params import TrainParams
import urllib.request
import wget

from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class PipelineParams:
    input_data_path: str
    downloading_params: DownloadParams
    train_params: TrainParams


PipelineParamsSchema = class_schema(PipelineParams)


def read_pipeline_params(path: str) -> PipelineParams:
    with open(path, "r") as input_stream:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))


a = read_pipeline_params("/Users/artemsnad/artemsnad/MADE/1_semester/mlops/hometasks/01/artem_snadin/homework1/configs/train_config.yaml")

print(a.downloading_params.storage)

with urllib.request.urlopen(a.downloading_params.storage) as f:
    b = f.read().decode('utf-8')
print(b)

wget.download(a.downloading_params.storage, 'test.csv')