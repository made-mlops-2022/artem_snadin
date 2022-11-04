# -*- coding: utf-8 -*-
from typing import Tuple, NoReturn
import os

import pandas as pd
from sklearn.model_selection import train_test_split
from params import SplittingParams

import wget


def download_data(storage: str, output: str) -> NoReturn:
    try:
        wget.download(storage, output)
    except FileExistsError:
        pass
    except ConnectionResetError:
        download_data(storage, output)


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def split_train_val_data(data: pd.DataFrame, params: SplittingParams) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data
