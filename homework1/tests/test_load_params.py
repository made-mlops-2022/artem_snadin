import os
from project import download_data, read_pipeline_params, TrainParams, ModelManager, Model
import pytest
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


CONFIG_PATH = "configs/train_config_1.yaml"


def test_dataset_download():
    try:
        pipeline_params = read_pipeline_params(CONFIG_PATH)
        downloading_params = pipeline_params.downloading_params
        os.makedirs(downloading_params.output_folder, exist_ok=True)
        output_path = os.path.join(downloading_params.output_folder, downloading_params.filename)
        if os.path.exists(output_path):
            os.remove(output_path)
        download_data(downloading_params.storage, output_path)
    except BaseException as ex:
        print(ex)
        assert False

    assert os.path.exists(output_path)


def test_models_load_error():
    train_params = TrainParams(model="", model_types=["abracadabra"], random_state=0, metrics="all")
    with pytest.raises(ValueError):
        ModelManager.load_models(train_params)


def test_models_load_success():
    train_params = TrainParams(model="LinearRegression", model_types=["LinearRegression", "RandomForestRegressor"], random_state=255, metrics="all")
    ModelManager.load_models(train_params)
    assert isinstance(ModelManager.get_model("LinearRegression"), LinearRegression)
    assert isinstance(ModelManager.get_model("RandomForestRegressor"), RandomForestRegressor)


def test_init_wrong_model():
    wrong_name = "wong_name"
    train_params = TrainParams(model=wrong_name, model_types=["LinearRegression"], random_state=0, metrics="all")
    ModelManager.load_models(train_params)
    with pytest.raises(NotImplementedError):
        Model(ModelManager.get_model(train_params.model), train_params)
