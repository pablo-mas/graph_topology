import os
import yaml
from utils import get_config


config = get_config()

EXPERIMENT_NAME = config['experiment_name']
BASE_PATH = config["BASE_PATH"]

DATA_PATH = os.path.join(BASE_PATH, "data")

MORPHOLOGICAL_CSV_PATH = os.path.join(BASE_PATH, "csv/morphology")
TOPOLOGICAL_CSV_PATH = os.path.join(BASE_PATH, "csv/topology")

VIZUALIZATION_PATH = os.path.join(BASE_PATH, "vizualization")
VISUALIZATION_WSI_PATH = os.path.join(VIZUALIZATION_PATH, "wsis")
VISUALIZATION_GRAPH_PATH = os.path.join(VIZUALIZATION_PATH, "graphs")

WSI_ID = config["WSI_ID"]

MORPHOLOGICAL_PROPERTIES = config['MORPHOLOGICAL_PROPERTIES']
CENTROID_ID = config['CENTROID_ID']

VISUALIZATION_CENTROID = config['VISUALIZATION_CENTROID']
VISUALIZATION_GRAPH = config['VISUALIZATION_GRAPH']

GRAPH = config['GRAPH']