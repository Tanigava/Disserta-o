from pathlib import Path
 
# Raiz do repositório: diretório pai de src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
 
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
RESULTS = PROJECT_ROOT / "results"
FIGURES = RESULTS / "figures"
TABLES = RESULTS / "tables"
 
# Exemplos de arquivos esperados (ajuste os nomes aos seus arquivos reais)
CLINICAL_FILE = DATA_RAW / "data_clinical_patient.txt"
MAD_3000_FILE = DATA_PROCESSED / "dados_VST_MAD_3000.csv"
MAD_5000_FILE = DATA_PROCESSED / "Zscore_VST_MAD5000.csv"
MAD_10000_FILE = DATA_PROCESSED / "Zscore_VST_MAD10000.csv"
MAD_20000_FILE = DATA_PROCESSED / "Zscore_VST_MAD20000.csv"



import numpy as np
import hdbscan
import igraph as ig
import leidenalg
from sklearn.neighbors import NearestNeighbors
 
def run_hdbscan(X, min_cluster_size=15, min_samples=None):
    model = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        metric="euclidean"
    )
    return model.fit_predict(X), model
 
def run_leiden(X, n_neighbors=30, resolution=0.15, seed=42):
    nbrs = NearestNeighbors(n_neighbors=n_neighbors).fit(X)
    graph = nbrs.kneighbors_graph(mode="connectivity", include_self=False)
    sources, targets = graph.nonzero()
 
    g = ig.Graph(
        n=X.shape[0],
        edges=list(zip(sources, targets)),
        directed=False
    )
    g.simplify()
 
    partition = leidenalg.find_partition(
        g,
        leidenalg.RBConfigurationVertexPartition,
        resolution_parameter=resolution,
        seed=seed
    )
    return np.asarray(partition.membership)
