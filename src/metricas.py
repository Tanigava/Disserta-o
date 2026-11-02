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
from sklearn.manifold import trustworthiness
from sklearn.metrics import (
    silhouette_score,
    adjusted_rand_score,
    normalized_mutual_info_score
)
 
def evaluate_embedding(X_reference, X_embedding, n_neighbors=15):
    return trustworthiness(
        X_reference, X_embedding, n_neighbors=n_neighbors
    )
 
def evaluate_clusters(X_embedding, labels, y_reference=None):
    labels = np.asarray(labels)
    valid = labels != -1  # remove ruído do HDBSCAN para Silhouette
 
    n_clusters = len(np.unique(labels[valid]))
    silhouette = (
        silhouette_score(X_embedding[valid], labels[valid])
        if n_clusters > 1 and valid.sum() > 1 else np.nan
    )
 
    result = {
        "n_clusters": n_clusters,
        "silhouette": silhouette,
        "noise_percent": 100 * np.mean(labels == -1)
    }
 
    if y_reference is not None:
        result["ARI"] = adjusted_rand_score(y_reference, labels)
        result["NMI"] = normalized_mutual_info_score(y_reference, labels)
 
    return result
