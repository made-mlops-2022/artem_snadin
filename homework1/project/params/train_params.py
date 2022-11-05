from dataclasses import dataclass
from typing import List


@dataclass()
class TrainParams:
    model_types: List[str]
    random_state: int
    model: str
    metrics: str
