import os
import numpy as np
import pandas as pd
import glob
from scipy import ndimage
from tqdm import tqdm
from skimage.measure import regionprops, regionprops_table
from skimage.segmentation import clear_border
from skimage.measure import label
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image

from params import DATA_PATH, MORPHOLOGICAL_CSV_PATH, TOPOLOGICAL_CSV_PATH, VISUALIZATION_WSI_PATH, VISUALIZATION_GRAPH_PATH, WSI_ID, MORPHOLOGICAL_PROPERTIES, CENTROID_ID, VISUALIZATION_CENTROID, VISUALIZATION_GRAPH, GRAPH
from utils import plot_centroids, plot_graph, compute_graph


if __name__ == "__main__":
    
    os.makedirs(MORPHOLOGICAL_CSV_PATH, exist_ok=True)
    os.makedirs(TOPOLOGICAL_CSV_PATH, exist_ok=True)
    os.makedirs(VISUALIZATION_WSI_PATH, exist_ok=True)
    os.makedirs(VISUALIZATION_GRAPH_PATH, exist_ok=True)
    
    if WSI_ID == "all":
        predictions_paths = sorted(glob.glob(DATA_PATH + "/*"))
    elif type(WSI_ID) == list:
        try: 
            predictions_paths = sorted(glob.glob(DATA_PATH + "/*"))
            predictions_paths = [predictions_paths[i] for i in WSI_ID]
        except:
            print('Not a valid WSI_ID list in config.yml')
    else : 
        print('Not a valid WSI_ID value in config.yml')
    
    
    for path in tqdm(predictions_paths):
        
        wsi_name = path.split('/')[-1] # get name of wsi from folder's name
        df = pd.DataFrame() # instantiate empty dataframe to store morphological features of one specific wsi
        images_paths = sorted(glob.glob(path + '/*.png')) # get the path to each patch of the wsi
                            
        for i, patch_path in tqdm(enumerate(images_paths), leave=False):
            
            xcoord = patch_path.split('/')[-1][:-4].split('_')[-2] # requires to have a standard naming convention of patch_paths (data/wsi_name/wsi_name_xcoord_ycoord.png)
            ycoord = patch_path.split('/')[-1][:-4].split('_')[-1]
            
            image = np.array(Image.open(patch_path)) # load patch as numpy array
            instance_map = label(ndimage.binary_opening(image, iterations=3)) # quick data processing to remove small objects and close small holes
            
            regions = regionprops(instance_map)
            tmp_df_1 = pd.DataFrame() # temporary dataframe to store properties of one region
            
            for j, props in enumerate(regions):
                tmp_df_2 = pd.DataFrame(regionprops_table(instance_map, properties=MORPHOLOGICAL_PROPERTIES))
                
                if CENTROID_ID : # give an id to each centroid if specified in config.yml
                    centroid_id = patch_path.split('/')[-1][:-4] + f'_{j}'
                    tmp_df_2['centroid_id'] = centroid_id
                    
                tmp_df_2['centroid-0'] += int(xcoord)
                tmp_df_2['centroid-1'] += int(ycoord)
                
                tmp_df_1 = pd.concat([tmp_df_1, tmp_df_2], ignore_index=True)
                
            df = pd.concat([df, tmp_df_1], ignore_index=True)
            
        df.drop_duplicates(inplace=True) # in case there are duplicated rows, remove them
        df.to_csv(os.path.join(MORPHOLOGICAL_CSV_PATH, f'{wsi_name}.csv'), index=False) # save dataframe with all the morphological features of one wsi
        
        if GRAPH['dropout'] > 0:
            df = df.sample(frac=GRAPH['dropout'])
            
        if VISUALIZATION_CENTROID['active']:
            plot_centroids(df=df,
                           wsi_name=wsi_name,
                           save_path=VISUALIZATION_WSI_PATH,
                           figsize=VISUALIZATION_CENTROID['figsize'],
                           size=VISUALIZATION_CENTROID['size'],
                           title=VISUALIZATION_CENTROID['title'],
                           dpi=VISUALIZATION_CENTROID['dpi'])
            

        G, pos = compute_graph(df=df, weight=GRAPH['weight'])

        if VISUALIZATION_GRAPH['active']:
            plot_graph(G=G, 
                       pos=pos, 
                       wsi_name=wsi_name,
                       save_path=VISUALIZATION_GRAPH_PATH,
                       figsize=VISUALIZATION_GRAPH['figsize'],
                       title=VISUALIZATION_GRAPH['title'],
                       dpi=VISUALIZATION_GRAPH['dpi'],
                       axis=VISUALIZATION_GRAPH['axis'],
                       options=VISUALIZATION_GRAPH['options'],
                       dropout=GRAPH['dropout'])
            
                       
            