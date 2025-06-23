import os
from kaggle.api.kaggle_api_extended import KaggleApi

# To start the API
api = KaggleApi()
api.authenticate()

# Dataset to download
dataset = "ishanshrivastava28/tata-online-retail-dataset"  # dataset name from kaggle

# Output directory
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "..", "data", "raw")
os.makedirs(output_dir, exist_ok=True)

# Code for download and unzip dataset
print("Downloading dataset...")
api.dataset_download_files(dataset, path=output_dir, unzip=True)
print("✅ Dataset downloaded and uncompressed in", output_dir)
