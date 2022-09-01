# Morphological and graph topological features extraction

## Introduction

This repository contains the code to extract morphological features from WSI, compute the associated Delaunay graph and extract topologicla features from it. 

## Prerequisites







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
└── params.py                           <span style="color:green">// parameters files that process config's information </span>