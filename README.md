# Morphological and graph topological features extraction

## Introduction

This repository contains the code to extract morphological features from WSI, compute the associated Delaunay graph and extract topological features from it. The code is ready to use and user-friendly thanks to the **config.yml** file. 

## Prerequisites

This code runs on **Python 3.8.12** but it is not guaranteed to work for newer versions. 

### Conda installation
Run the following command to create a new environment with the correct Python version and necessary packages using conda.

```bash
conda create -n graph python=3.8.12 
conda install --file requirements.txt
```

### Pyenv + virtualenv installation
Run the following command to create a new environment with the correct Python version and necessary packages using pyenv, virtualenv and pip.

```bash
pyenv virtualenv 3.8.12 graph
pip install -r requirements.txt
```

# How to setup and run an experiment
This code was made to be easy-to-use, requiring to only modify the **config.yml** file with the desired parameters. 

```yml
# config.yml file structure

EXPERIMENT_NAME : "exp1" # the experiment name

BASE_PATH : /home/pablo/code/aramis/graph_topology # path to the root of the folder

WSI_ID : "all" # set to "all" or a list containing the index of the WSIs to process (ex. [0, 2])

MORPHOLOGICAL_PROPERTIES : ['centroid', 'area', 'perimeter','area_bbox', 'area_convex', 'axis_major_length', 'axis_minor_length', 'eccentricity', 'extent', 'solidity'] # check https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops

TOPOLOGICAL_PROPERTIES : []

CENTROID_ID : False # Keep or not the centroid id in the csv files
UNET_THRESHOLD : 0.5

GRAPH:
  dropout: 0 # randomly drops a fraction of centroids before computing the graph
  weight: True # if set to True, the weight of the edge between two nodes is defined as 1/euclidean distance between the two. If False, weight is set to 1 for all edges.

VISUALIZATION_CENTROID :
  active : True # to save the visualization plot or not
  title : True # set title or not
  figsize : 20 # figsize (square of size figsize)
  size: 2 # size of the dots representing each centroid
  dpi: 300 # dpi of the saved image

VISUALIZATION_GRAPH :
  active : True # to save the visualization plot or not
  title : True # set title or not
  figsize : 20 # figsize (square of size figsize)
  dpi: 300 # dpi of the saved image
  axis: False
  options: 
    font_size: 0
    node_size: 25
    node_color: 'blue'
    edgecolors: black
    linewidths: 1
    width: 1

```

Once the configuration file is ready, you just have to launch the main.py file.

```bash
python main.py
```


# Repository structure
The data from the U-Net inference should be stored in the data folder, in subfolders corresponding to each WSI. It is essential that the predictions are in **.npy** format with the following nomenclature : **wsi_name_xcoord_ycoord**. 

The results will then be stored in folders with the name of the experiment defined in the configuration file. 


<pre>
├── data                                <span style="color:green">// contains U-Net's inference data</span>
│   ├── wsi_1                           
│   │   ├── wsi1_xcoord1_ycoord1.npy
│   │   ├── wsi1_xcoord2_ycoord2.npy
│   │   └── ...
│   ├── wsi_2 
│   └── wsi_3
├─ results                              <span style="color:green">// folder containing U-Net's inference data </span>    
│   ├── exp_1  
│   │   ├── csv  
│   │   │   ├── morphology                         
│   │   │   │   ├── morphology_wsi_1.csv
│   │   │   │   ├── morphology_wsi_2.csv
│   │   │   │   └── morphology_wsi_3.csv
│   │   │   └── topology                         
│   │   │        └── topology_exp_1.csv
│   │   │
│   │   └── visualization 
│   │       ├── graphs                        
│   │       │   ├── wsi_1.png
│   │       │   ├── wsi_2.png
│   │       │   └── wsi_3.png
│   │       └── wsis                         
│   │           ├── wsi_1.png
│   │           ├── wsi_2.png
│   │           └── wsi_3.png 
│   ├── exp_2
│   ├── exp_3
│   └── ...
│
├── config.yml                          <span style="color:green">// config file to modify </span> 
├── main.py                             <span style="color:green">// file to run </span>
├── params.py                           <span style="color:green">// parameters file that process config's information </span>
└── utils.py                            <span style="color:green">// useful functions </span>