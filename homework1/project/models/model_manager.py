"""Model Manager class for loading, managing, and interacting with models."""
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
try:
    from params import TrainParams
except ModuleNotFoundError:
    from ..params import TrainParams


class ModelManager(object):
    """Singleton class that instantiates and manages model objects."""

    _models = {}

    @classmethod
    def load_models(cls, params: TrainParams):
        """Load models from configuration."""
        cls._models = {}
        for model_type in params.model_types:
            try:
                if model_type == "RandomForestRegressor":
                    model_module = eval(model_type)(n_estimators=100, random_state=params.random_state)
                else:
                    model_module = eval(model_type)()
                cls._models[model_type] = model_module
            except BaseException:
                raise ValueError(model_type)

    @classmethod
    def get_models(cls) -> dict:
        return cls._models

    @classmethod
    def get_model(cls, qualified_name):
        model = None
        try:
            model = cls._models[qualified_name]
        except KeyError:
            pass
        return model
