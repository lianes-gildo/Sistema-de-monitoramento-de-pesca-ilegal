# =====================================================
# Geração de CSV sintético balanceado - 500 linhas
# =====================================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Configurar semente
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Número de amostras
n_amostras = 500

# Listas auxiliares
provincias = ["Maputo", "Inhambane", "Sofala", "Zambézia", "Nampula"]
tipos_embarcacao = ["Pesqueiro", "Recreativo", "Industrial", "Artesanal"]
especies = ["Camarão", "Atum", "Pargo", "Lagosta", "Caranguejo"]
zonas_marinha = ["Zona Norte", "Zona Centro", "Zona Sul", "Zona Proibida"]
tipos_infracao = ["Pesca fora da licença", "Zona proibida", "Captura proibida"]

# IDs e nomes
ids = np.arange(1, n_amostras + 1)
nomes_emb = [f"Barco_{i:03d}" for i in ids]
datas = [datetime(2025,10,22) - timedelta(days=random.randint(0,30)) for _ in range(n_amostras)]
provincias_rand = [random.choice(provincias) for _ in range(n_amostras)]
tipos_emb = [random.choice(tipos_embarcacao) for _ in range(n_amostras)]
especies_capt = [random.choice(especies) for _ in range(n_amostras)]
quantidade = [round(random.uniform(50,1000),2) for _ in range(n_amostras)]

# Variáveis da RNA e infração
licenca = []
ais = []
velocidade = []
distancia = []
hora = []
ocorrencia = []
tipo_infracao_col = []
zonas = []

for i in range(n_amostras):
    if i < n_amostras//2:
        # 250 legais
        licenca.append(1)
        ais.append(1)
        velocidade.append(round(random.uniform(5,15),2))
        distancia.append(round(random.uniform(10,40),2))
        hora.append(random.randint(5,19))
        ocorrencia.append(0)
        tipo_infracao_col.append("")
        zonas.append(random.choice(["Zona Norte","Zona Centro","Zona Sul"]))
    else:
        # 250 ilegais (padrão 100% probabilidade)
        licenca.append(0)
        ais.append(0)
        velocidade.append(round(random.uniform(0.5,5),2))
        distancia.append(round(random.uniform(50,100),2))
        hora.append(random.choice(list(range(0,5))+list(range(20,24))))
        ocorrencia.append(1)
        tipo_infracao_col.append(random.choice(tipos_infracao))
        zonas.append("Zona Proibida")

# Criar DataFrame final
dados = pd.DataFrame({
    "id_registo": ids,
    "data_atividade": [d.strftime("%Y-%m-%d") for d in datas],
    "provincia": provincias_rand,
    "nome_embarcacao": nomes_emb,
    "tipo_embarcacao": tipos_emb,
    "licenca_valida": licenca,
    "especie_capturada": especies_capt,
    "quantidade_kg": quantidade,
    "zona_marinha": zonas,
    "sinal_AIS_detectado": ais,
    "velocidade_nos": velocidade,
    "distancia_costa_km": distancia,
    "hora_atividade": hora,
    "ocorrencia_infracao": ocorrencia,
    "tipo_infracao": tipo_infracao_col
})

# Salvar CSV no diretório atual
caminho_saida = os.path.join(os.getcwd(), "pesca_mocambique_analise.csv")
dados.to_csv(caminho_saida, index=False, encoding='utf-8')

print(f"✅ CSV balanceado de 500 linhas gerado em: {caminho_saida}")
print("\nAmostra (primeiras 10 linhas):")
print(dados.head(10).to_string(index=False))
