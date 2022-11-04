from dataclasses import dataclass


@dataclass()
class TrainParams:
    model_type: str
    random_state: int
