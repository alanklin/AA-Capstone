### _setup.py ###
# This file is used to handle the imports of the notebooks for ease of use and consistency with 
# variable names. Should be called at the top of the notebooks.

# @author AL, TP

import subprocess
import sys
import os
from pathlib import Path

# Function to install dependencies
def install_requirements(requirements_file="requirements.txt"):
    """Installs dependencies from a requirements.txt file."""
    if os.path.exists(requirements_file):
        print(f"Installing dependencies from {requirements_file}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("All dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)
    else:
        print(f"Error: {requirements_file} not found!")
        sys.exit(1)

# Run dependency installation
install_requirements()

# Get the absolute path to the current script (_setup.py)
script_dir = Path(__file__).resolve().parent

# Get the project root (assuming Notebooks is at the same level as data)
project_root = script_dir.parent.parent

# Construct the path to data.csv
sector_data_csv_path = project_root / "Data" / "sector_encounters_fy_2020_2025.csv"
sector_data_csv_path_train = project_root / "Data" / "sector_encounters_train.csv"
sector_data_csv_path_test = project_root / "Data" / "sector_encounters_test.csv"
state_data_csv_path = project_root / "Data" / "Border_State_Data.csv"
state_data_csv_path_cleaned = project_root / "Data" / "state_encounters_cleaned.csv"
state_data_train = project_root / "Data" / "state_train.csv"
state_data_test = project_root / "Data" / "state_test.csv"

sector_train_dropped_csv_path = project_root / "Data" / "sector_train_dropped.csv"

# Data manipulation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import seaborn as sns

# For mapping use:
import geopandas as gpd
import geopandas.tools

# Statistical methods
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

# Feature Engineering
from sklearn.preprocessing import OneHotEncoder