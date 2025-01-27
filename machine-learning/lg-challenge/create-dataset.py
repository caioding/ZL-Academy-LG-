import pandas as pd
import numpy as np

# Definir número de registros
n_samples = 1000

# Gerar dados aleatórios
np.random.seed(42)
data = {
    "Power Consumption (kW)": np.round(np.random.uniform(1.0, 6.0, n_samples), 2),
    "Cooling Capacity (BTU)": np.random.choice([9000, 12000, 18000, 24000, 30000], n_samples),
    "Noise Level (dB)": np.round(np.random.uniform(35, 60, n_samples), 2),
    "EER": np.round(np.random.uniform(2.5, 4.5, n_samples), 2),
    "Temperature Range (°C)": np.random.choice([15, 18, 20, 25, 30], n_samples),
    "Airflow (m³/min)": np.round(np.random.uniform(8, 30, n_samples), 2),
    "Warranty (Years)": np.random.choice([2, 3, 4, 5, 6], n_samples),
    "Build Quality Rating": np.random.randint(1, 11, n_samples),
    "Maintenance Cost ($)": np.random.randint(100, 500, n_samples),
    "Type": np.random.choice([0, 1], n_samples),  # 0 = Outdoor, 1 = Indoor
}

# Criar coluna de "Efficiency Score" como target de regressão
data["Efficiency Score"] = (
    (data["EER"] * 20)
    + (10 - data["Noise Level (dB)"] / 10)
    + (data["Build Quality Rating"] * 2)
    - (data["Maintenance Cost ($)"] / 50)
    + np.random.uniform(-5, 5, n_samples)
).astype(int)

# Garantir valores dentro de limites
data["Efficiency Score"] = np.clip(data["Efficiency Score"], 0, 100)

# Criar DataFrame
dataset = pd.DataFrame(data)

# Salvar como CSV
import os

current_dir = os.getcwd()
path_file = os.path.join(current_dir, "machine-learning/lg-challenge/product_quality_dataset.csv")
dataset.to_csv(path_file, index=False)

print(f"Dataset salvo em: {path_file}")