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




from sklearn.decomposition import PCA
from umap import UMAP

from pacmap import PaCMAP
 
def run_pca(X, n_components=50, random_state=42):
    n_comp = min(n_components, X.shape[1], X.shape[0] - 1)
    model = PCA(n_components=n_comp, random_state=random_state)
    return model.fit_transform(X), model
 
def run_umap(X, n_neighbors, min_dist, random_state=42):
    model = UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        random_state=random_state
    )
    return model.fit_transform(X), model
 
def run_pacmap(X, n_neighbors, mn_ratio, fp_ratio, random_state=42):
    model = PaCMAP(
        n_neighbors=n_neighbors,
        MN_ratio=mn_ratio,
        FP_ratio=fp_ratio,
        random_state=random_state
    )
    return model.fit_transform(X), model
