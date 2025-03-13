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
project_root = script_dir.parent.parent

# Construct the path to data.csv
sector_data_csv_path = project_root / "Data" / "sector_encounters_fy_2020_2025.csv"

sector_data_csv_path_train = project_root / "Data" / "sector_encounters_train.csv"
sector_data_csv_path_test = project_root / "Data" / "sector_encounters_test.csv"

sector_data_csv_path_train_pivoted = project_root / "Data" / "sector_encounters_train_pivot.csv"
sector_data_csv_path_test_pivoted = project_root / "Data" / "sector_encounters_test_pivot.csv"

# TODO : Fix naming convention on these, they may be useless
# sector_train_input_ready = project_root / "Data" / "sector_train_input_ready.csv"
# sector_train_dropped_csv_path = project_root / "Data" / "sector_train_dropped.csv"

state_data_csv_path = project_root / "Data" / "Border_State_Data.csv"
state_data_csv_path_cleaned = project_root / "Data" / "state_encounters_cleaned.csv"
state_data_train = project_root / "Data" / "state_train.csv"
state_data_test = project_root / "Data" / "state_test.csv"

scalers_file = project_root / "Data" / "scalers.pickle"

# Model outputs in Week 7
hyperparameters_file = project_root / "Model_Outputs" / "hyperparameter_configs.txt"
nn_mape_results_file = project_root / "Model_Outputs" / "nn_model_results.pkl" 
nn_mape_results_file1 = project_root / "Model_Outputs" / "nn_model_results1.pkl" 
nn_mape_results_file2 = project_root / "Model_Outputs" / "nn_model_results2.pkl" 

lstm_mape_results_file = project_root / "Model_Outputs" / "lstm_model_results.pkl"
lstm_mape_results_file1 = project_root / "Model_Outputs" / "lstm_model_results1.pkl"
lstm_mape_results_file2 = project_root / "Model_Outputs" / "lstm_model_results2.pkl"
lstm_mape_results_file3 = project_root / "Model_Outputs" / "lstm_model_results3.pkl"


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

# Scaling
from sklearn.preprocessing import MinMaxScaler

# Transformer Model

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Dropout, InputLayer, LSTM
from tensorflow.keras.callbacks import EarlyStopping