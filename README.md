# RBras — Análise de dados de RNA-seq de câncer de mama
 
## Objetivo
Investigar como a filtragem de genes por variabilidade (MAD) influencia
a redução de dimensionalidade e a identificação de agrupamentos em dados
de bulk RNA-seq do TCGA-BRCA.
 
## Métodos
- Filtragem por MAD: 3.000, 5.000, 10.000 e 20.000 genes
- PCA: 50 componentes
- Redução de dimensionalidade: UMAP e PaCMAP
- Agrupamento: Leiden e HDBSCAN
- Avaliação: Trustworthiness, Silhouette, ARI e NMI
- Estabilidade: avaliação dos modelos selecionados em dez sementes
 
## Organização
- `src/`: funções reutilizáveis
- `scripts/`: execução das análises
- `notebooks/`: exploração e visualização
- `results/figures/`: figuras finais
 
## Dados
Os dados não estão incluídos neste repositório. Consulte `data/README.md`
para instruções de obtenção e preparação, respeitando os termos de uso
e as regras aplicáveis ao TCGA/GDC.
 
## Ambiente
Crie e ative um ambiente virtual e instale as dependências:
 
```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Reprodutibilidade
Consulte os scripts para parâmetros, sementes aleatórias e critérios
de seleção dos modelos.
