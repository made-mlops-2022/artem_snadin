from typing import Dict
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.pipeline import Pipeline

try:
    from params import TrainParams
except ModuleNotFoundError:
    from ..params import TrainParams


class Model:
    def __init__(self, model,  train_params: TrainParams):
        self._model = model
        if self._model is None:
            raise NotImplementedError()
        self._metrics = train_params.metrics
        self._pipeline = None

    def train(self, features: pd.DataFrame, target: pd.Series):
        self._model.fit(features, target)

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        if self._pipeline is None:
            predicts = self._model.predict(features)
        else:
            predicts = self._pipeline.predict(features)
        return predicts

    def evaluate(self, predicts: np.ndarray, target: pd.Series) -> Dict[str, float]:
        result = {}
        if self._metrics == "r2_score":
            result["r2_score"] = r2_score(target, predicts)
        elif self._metrics == "rmse":
            result["rmse"] = mean_squared_error(target, predicts, squared=False)
        elif self._metrics == "mae":
            result["mae"] = mean_absolute_error(target, predicts)
        elif self._metrics == "all":
            result = {
                "r2_score": r2_score(target, predicts),
                "rmse": mean_squared_error(target, predicts, squared=False),
                "mae": mean_absolute_error(target, predicts),
            }
        return result

    def create_inference_pipeline(self, transformer: ColumnTransformer) -> Pipeline:
        self._pipeline = Pipeline([("feature_part", transformer), ("model_part", self._model)])

