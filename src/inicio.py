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
