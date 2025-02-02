
### _setup.py ###
# This file is used to handle the imports of the notebooks for ease of use and consistency with 
# variable names. Should be called at the top of the notebooks.

# @author AL, TP

# File paths
from pathlib import Path
# Get the absolute path to the current script (_setup.py)
script_dir = Path(__file__).resolve().parent

# Get the project root (assuming Notebooks is at the same level as data)
project_root = script_dir.parent.parent

# Construct the path to data.csv
sector_data_csv_path = project_root / "Data" / "sector_encounters_fy_2020_2025.csv"
state_data_csv_path = project_root / "Data" / "Border_State_Data.csv"


# Data manipulation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, os
import seaborn as sns

# For mapping use:
import geopandas as gpd
import geopandas.tools
