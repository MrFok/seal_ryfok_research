import sys
sys.path.insert(0,sys.path[0] + "\\..\\src")

from gretel_ai.gretel_actgan import *
import time
import pandas as pd
from smart_open import open

"""
    NOTE: You will need to have set up and install the Gretel Python SDK before running this script.
          For more information, see https://docs.gretel.ai/guides/environment-setup/cli-and-sdk

           You will also need to have available credits in your Gretel account to generate more synthetic
           data. 
"""

# Set project name and model id of a previously trained model
PROJECT_NAME = "NaturalFuzzTest"
MODEL_ID = "653864c07b3d02c8466f09fb"

# Obtain GretelProject object
print("Retrieving project: " + PROJECT_NAME)
actgan_project = GretelACTGAN(PROJECT_NAME)
print("Project retrieved")

# Retrieve the model
# NOTE: You can find the model IDs in the "Records & downloads" section
#       of the Gretel model console. I have not found a way to retrieve
#       the model ID within the python SDK
print("Retrieving model: " + MODEL_ID)
model = actgan_project.retrieve_model(MODEL_ID)
print("Model retrieved")

# Preview data
synthetic_df = pd.read_csv(actgan_project.get_model().get_artifact_link("data_preview"), compression="gzip")
print(synthetic_df)

# Get URL for model report
print("Model report URL: " + actgan_project.get_model().get_artifact_link("report"))
# TODO: Fix IPython import
# actgan_project.download_csv_artifact(artifact="report")
# show_report = input("Do you want to view the model report? (y/n): ")

# if show_report == "y":
#     # Open model report in default browser
#     IPython.display.HTML(data=open(model.get_artifact_link("report")).read(), metadata=dict(isolated=True))

# Ask user if they want to generate synthetic data
generate_data = input("Do you want to generate synthetic data? (y/n): ")
num_records = input("How many records do you want to generate? (integer): ")

if generate_data == "y":
    # Generate synthetic data
    print("Sending query...")
    new_synthetic_df = actgan_project.generate_synthetic_data(num_records, 200, verbose = False, download = True)




