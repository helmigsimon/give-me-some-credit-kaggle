import os
import pathlib

CONFIG_PATH = pathlib.Path(os.path.abspath(__name__))
GMC_PATH = CONFIG_PATH.parent
ROOT = GMC_PATH.parent
DATA_PATH = ROOT / "data"
INPUT_DATA_PATH = DATA_PATH/'input'

