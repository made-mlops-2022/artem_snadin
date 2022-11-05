from project import TrainParams, ModelManager, Model
import pytest
import pandas as pd
from typing import Tuple
import random
import numpy as np


def _gen_test_data_plus(min_val: int, max_val: int, amount: int) -> Tuple[pd.DataFrame, pd.Series]:
    x1 = np.array([random.randint(min_val, max_val) for _ in range(amount)])
    x2 = np.array([random.randint(min_val, max_val) for _ in range(amount)])
    f = {"x1": x1, "x2": x2}
    features = pd.DataFrame(f)
    t = x1 + x2
    target = pd.Series(t)
    return features, target


def _gen_test_data_minus(min_val: int, max_val: int, amount: int) -> Tuple[pd.DataFrame, pd.Series]:
    x1 = np.array([random.randint(min_val, max_val) for _ in range(amount)])
    x2 = np.array([random.randint(min_val, max_val) for _ in range(amount)])
    f = {"x1": x1, "x2": x2}
    features = pd.DataFrame(f)
    t = x1 - x2
    target = pd.Series(t)
    return features, target


@pytest.mark.parametrize("test_model_name", ["LinearRegression", "RandomForestRegressor"])
def test_model_predict(test_model_name):
    n = 100
    train_params = TrainParams(model=test_model_name, model_types=[test_model_name], random_state=255, metrics="all")
    ModelManager.load_models(train_params)
    test_model = Model(ModelManager.get_model(test_model_name), train_params)
    train_features, train_target = _gen_test_data_plus(0, 100, n)
    test_model.train(train_features, train_target)
    val_features, val_target = _gen_test_data_plus(0, 100, n)
    predicts = test_model.predict(val_features)
    print(predicts)
    print(val_target)
    assert np.allclose(predicts, val_target, rtol=10)

    val_features, val_target = _gen_test_data_minus(0, 100, n)
    predicts = test_model.predict(val_features)
    assert not np.allclose(predicts, val_target, rtol=10)
