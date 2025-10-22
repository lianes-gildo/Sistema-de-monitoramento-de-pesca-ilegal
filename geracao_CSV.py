# ============================
# Núcleo 1 - Gerar dataset aumentado (500 linhas)
# ============================

import pandas as pd
import numpy as np
import random

# Número total de amostras
n_amostras = 500

# IDs e nomes dos barcos
ids = np.arange(1, n_amostras + 1)
nomes = [f"Barco_{i:03d}" for i in ids]

# Listas para variáveis
licenca = []
ais = []
velocidade = []
distancia = []
hora = []
infracao = []

for i in range(n_amostras):
    if i < n_amostras / 2:
        # Barcos legais
        licenca.append(1)
        ais.append(1)
        velocidade.append(round(random.uniform(5, 15), 2))
        distancia.append(round(random.uniform(10, 40), 2))
        hora.append(random.randint(5, 19))
        infracao.append(0)
    else:
        # Barcos ilegais
        licenca.append(0)
        ais.append(0)
        velocidade.append(round(random.uniform(0.5, 5), 2))
        distancia.append(round(random.uniform(50, 100), 2))
        hora.append(random.choice(list(range(0, 5)) + list(range(20, 24))))
        infracao.append(1)

# Criar DataFrame
dados = pd.DataFrame({
    "id_barco": ids,
    "nome_barco": nomes,
    "licenca_ativa": licenca,
    "sinal_AIS": ais,
    "velocidade_nos": velocidade,
    "distancia_costa_km": distancia,
    "hora_dia": hora,
    "ocorrencia_infracao": infracao
})

# Salvar CSV
dados.to_csv("/content/pesca_ilegal_mocambique_500.csv", index=False)
print("✅ Dataset aumentado gerado e salvo como pesca_ilegal_mocambique_500.csv")
dados.head(10)
