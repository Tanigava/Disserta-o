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



import pandas as pd
import numpy as np
 
COLUNAS_CLINICAS = {
    "PAM50", "SUBTYPE", "CLASS", "ROTULO", "BRCA_SUBTYPE"
}
 
def load_expression_matrix(path):
    """Carrega matriz e padroniza para amostras nas linhas e genes nas colunas."""
    df = pd.read_csv(path, index_col=0)
    df.index = df.index.astype(str).str.replace(".", "-", regex=False)


    # Regra heurística usada no script original; confira a orientação
    # com as dimensões e os identificadores do arquivo antes de confiar nela.
    if df.shape[0] > df.shape[1]:
        df = df.T
 
    df = df.drop(
        columns=[c for c in df.columns
                 if str(c).upper() in COLUNAS_CLINICAS],
        errors="ignore"
    )
    return df
 
def load_pam50_labels(path):
    clinical = pd.read_csv(
        path, comment="#", sep="\t", index_col="PATIENT_ID"
    )
    clinical.index = clinical.index.astype(str).str.replace(".", "-", regex=False)
    clinical["SUBTYPE"] = clinical["SUBTYPE"].fillna("Desconhecido")
 
    labels = {
        str(patient_id)[:12]: row["SUBTYPE"]
        for patient_id, row in clinical.iterrows()
    }
    return labels
 
def map_labels(sample_ids, subtype_dict):
    return np.array([
        subtype_dict.get(str(sample_id)[:12], "Desconhecido")
        for sample_id in sample_ids
    ])


import numpy as np
import pandas as pd
 
def select_top_mad_genes(X, n_genes):
    """Seleciona as n_genes colunas com maior MAD.
 
    X deve ter amostras nas linhas e genes nas colunas.
    """
    mad = X.apply(
        lambda col: np.median(np.abs(col - np.median(col))),
        axis=0
    )
    selected = mad.nlargest(min(n_genes, X.shape[1])).index
    return X.loc[:, selected], mad.loc[selected]
