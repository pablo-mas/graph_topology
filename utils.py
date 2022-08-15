import yaml
import matplotlib.pyplot as plt
import os
import networkx as nx
import numpy as np
from libpysal.cg import voronoi_frames
from libpysal import weights, examples
from scipy.spatial import distance


def get_config():
    with open('config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def plot_centroids(df, wsi_name, save_path, figsize=20, size=2, title=True, dpi=300):
    fig, ax = plt.subplots(1, 1, figsize=(figsize, figsize))
    ax.scatter(x=df['centroid-0'], y=df['centroid-1'], s=size)
    if title: 
        ax.set_title(f'{wsi_name}')
    plt.savefig(os.path.join(save_path, f'{wsi_name}.png'), dpi=dpi)
    plt.close()
    
def plot_graph(G, pos, wsi_name, save_path, options, figsize=10, title=True, dpi=300, axis=False, dropout=False, ):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    fig.patch.set_facecolor('white')
    options=options
    
    nx.draw_networkx(G, pos, ax=ax, **options)
    
    if title:
        ax.set_title(f'{wsi_name}')
    if title and dropout > 0: 
        ax.set_title(f'{wsi_name} with dropout = {dropout}')
    if not axis:    
        ax.axis('off')
        
    plt.savefig(os.path.join(save_path, f'{wsi_name}.png'), dpi=dpi)
    plt.close()
    
def compute_graph(df, weight):
    centroids = df[['centroid-0', 'centroid-1']].values
    points = [(float(x[0]), float(x[1])) for x in centroids]
    points_array = np.array(points)
    x_max = points_array[:, 0].max()
    y_max = points_array[:, 1].max()
    divider = np.array([x_max, y_max])
    points = [(float(x[0]), float(x[1])) for x in points_array / divider]
    pos = {i: point for i, point in enumerate(points)}
    cells, generators = voronoi_frames(points)
    
    delaunay = weights.Rook.from_dataframe(cells)
    G = delaunay.to_networkx()

    weighted_G = nx.Graph()
    weighted_G.add_nodes_from(G.nodes())
    
    if weight:
        for edges in G.edges():
            weighted_G.add_edge(*edges, weight=1/distance.euclidean(centroids[edges[0]], centroids[edges[1]]))
    else:
        for edges in G.edges():
            weighted_G.add_edge(*edges, 1)

    G = weighted_G.copy()
    
    return G, pos
