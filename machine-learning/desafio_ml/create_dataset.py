import numpy as np
import pandas as pd

# Creating a fictitious dataset with numerical data for quality metrics of air conditioners
np.random.seed(42)  # For reproducibility

# Number of samples to generate
n_samples = 1000

# Generating numerical data for air conditioners (indoor and outdoor)
quality_data = pd.DataFrame({
    "product_id": np.random.randint(1, 101, size=n_samples),  # Product IDs from 1 to 100
    "defect_type": np.random.randint(1, 4, size=n_samples),  # Encoding defect types as integers (1, 2, 3)
    "defect_location": np.random.randint(1, 3, size=n_samples),  # Encoding locations (1=Indoor, 2=Outdoor)
    "severity": np.random.randint(1, 4, size=n_samples),  # Encoding severity levels (1=Minor, 2=Major, 3=Critical)
    "inspection_method": np.random.randint(1, 4, size=n_samples),  # Inspection methods as integers (1, 2, 3)
    "energy_efficiency": np.random.uniform(10, 30, size=n_samples),  # Energy efficiency ratings
    "noise_level": np.random.uniform(20, 60, size=n_samples),  # Noise level in decibels
    "repair_cost": np.random.uniform(100, 1000, size=n_samples),  # Repair cost in USD
    "cooling_capacity": np.random.uniform(1.5, 5.0, size=n_samples)  # Cooling capacity in kW
})

# Previewing the first few rows of the generated dataset
quality_data.head()

import os
import pandas as pd

current_dir = os.getcwd()
path_file = os.path.join(current_dir, "quality_metrics_air_conditioners.csv")

quality_data.to_csv(path_file, index=False)

path_file