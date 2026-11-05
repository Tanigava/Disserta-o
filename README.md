# Dissertação de Mestrado — Análise de dados de RNA-seq de câncer de mama
 
## Objetivo
Comparar os resultados obtidos ao otimizar a redução de dimensionalidade em conjunto com o agrupamento diante a otimização separada da redução de dimensionalidade e logo em seguida do agrupamento.

## Métodos
- Filtragem por MAD: 5.000 genes
- PCA: 50 componentes
- Redução de dimensionalidade: PaCMAP
- Agrupamento: GMM
 
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
