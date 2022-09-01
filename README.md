# Morphological and graph topological extraction

## Introduction

This repository contains the code to extract morphological features from WSI, compute the associated Delaunay graph and extract topologicla features from it. 

## Prerequisites







<pre>
├── data <span style="color:green">// store features</span>
│   ├── morphology <span style="color:green">// store morphological features</span>
│   └── topology <span style="color:green">// store topological features</span>
├─ data <span style="color:green">// folder containing U-Net's inference data </span>    
├─ topology <span style="color:green">// morphological and topological features extraction </span>
│   ├─ params.py <span style="color:green">// store parameters and compute paths from config.yml</span>
│   ├─ utils.py <span style="color:green">// useful functions</span>
│   └─ main.py <span style="color:green">// compute graphs, extract morphological and topological features </span>
├─ notebooks <span style="color:green">// notebook examples with visualization</span>    
├─ visualization <span style="color:green">// where to save the output centroids and graphs images </span>    
└─ config.yml <span style="color:green">// config file </span>      
</pre>