from dataclasses import dataclass


@dataclass()
class DownloadParams:
    output_folder: str
    storage: str
    filename: str
