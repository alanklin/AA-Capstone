### _setup.py ###
# This file is used to handle the imports of the notebooks for ease of use and consistency with 
# variable names. Should be called at the top of the notebooks.

# @author AL, TP

import subprocess
import sys
import os
from pathlib import Path
import pickle

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
project_root = script_dir.parent
print(f"Project root directory is: {project_root}")

# Construct the path to data.csv
sector_data_csv_path = project_root / "Data" / "sector_encounters_fy_2020_2025.csv"

sector_data_csv_path_train = project_root / "Data" / "sector_encounters_train.csv"
sector_data_csv_path_test = project_root / "Data" / "sector_encounters_test.csv"

sector_data_csv_path_train_pivoted = project_root / "Data" / "sector_encounters_train_pivot.csv"
sector_data_csv_path_test_pivoted = project_root / "Data" / "sector_encounters_test_pivot.csv"

scalers_file = project_root / "Data" / "scalers.pickle"


# Model outputs in week 13, final models and predictions
final_output_folder = project_root / "Final_Outputs"
full_visualizations_folder = final_output_folder / "full_visualizations"
zoomed_visualizations_folder = final_output_folder / "zoomed_visualizations"
saved_models_folder = final_output_folder / "saved_models"

# Data manipulation
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sys
import os
import seaborn as sns
import itertools
import warnings


# Statistical methods
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA


# Scaling
from sklearn.preprocessing import MinMaxScaler
