import os
import marshmallow_dataclass
from project import download_data, read_pipeline_params

CONFIG_PATH = "configs/train_config.yaml"


def test_dataset_download():
    try:
        pipeline_params = read_pipeline_params(CONFIG_PATH)
        downloading_params = pipeline_params.downloading_params
        os.makedirs(downloading_params.output_folder, exist_ok=True)
        output_path = os.path.join(downloading_params.output_folder, downloading_params.filename)
        if os.path.exists(output_path):
            os.remove(output_path)
        download_data(downloading_params.storage, output_path)
    except BaseException:
        assert False

    assert os.path.exists(output_path)
