# Análise de dados de RNA-seq de câncer de mama

Projeto desenvolvido no contexto de uma dissertação de Mestrado em Matemática Aplicada e Computacional.

## Objetivo

Investigar estratégias de redução de dimensionalidade e agrupamento
não supervisionado em dados de expressão gênica de pacientes com
câncer de mama (TCGA-BRCA).

## Métodos

- Variance Stabilizing Transformation (VST)
- Median Absolute Deviation (MAD)
- PaCMAP
- Gaussian Mixture Models (GMM)
- Otimização de hiperparâmetros com Optuna

## Estratégias investigadas

1. Otimização conjunta de PaCMAP e GMM.
2. Otimização independente de PaCMAP e GMM.

## Tecnologias utilizadas

- Python
- NumPy
- Pandas
- Scikit-learn
- PaCMAP
- Optuna
- pyDRMetrics

## Estrutura

- `notebooks/`: notebooks de análise e experimentação.
- `src/`: funções e módulos auxiliares.
- `requirements.txt`: dependências do projeto.

## Execução

Instale as dependências com:

```bash
pip install -r requirements.txt