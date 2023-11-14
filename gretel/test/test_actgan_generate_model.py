import sys
sys.path.insert(0,sys.path[0] + "\\..\\src")

from gretel_ai.gretel_actgan import *
import time
import pandas as pd
import json
from gretel_client.helpers import poll

"""
    NOTE: You will need to have set up and install the Gretel Python SDK before running this script.
          For more information, see https://docs.gretel.ai/guides/environment-setup/cli-and-sdk

          You will also need to have available credits in your Gretel account to train your model.
          For reference, a 323MB data with ~1.5 million records with 34 fields took around 30 credits
          and 2+ hours to train.

          This generate model test only uses the cloud submission method, which utilizes
          Gretel's cloud infrastructure to train your model.
"""

# Set path of the dataset you want to generate a model with (This dataset "customer" is pretty small (12,000KB))
DATASET_PATH = "GretelTest\\data\\customer\\part-00000-018a18fa-e048-4775-a5f7-545a6df3e038-c000.csv"

# Set project name to access or generate
PROJECT_NAME = "NaturalFuzzTest"

# Create GretelProject object
print("Creating or retrieving project: " + PROJECT_NAME)
gretel = GretelACTGAN(PROJECT_NAME)

# Generate config
# standard config, auto epochs, 5000 records, dp=True, similarity="medium"
config_file = gretel.create_config(similarity = "medium", verbose = False)
# print(f"Model configuration:\n{json.dumps(config_file, indent=2)}")

# Create and submit model via cloud
# NOTE: no need to specify config_file, as create_config() saves it to the gretel object
print("Generating model...")
our_model = gretel.project.create_model_obj(model_config=config_file, data_source=DATASET_PATH)
start_time = time.time()
gretel.generate_model(dataset_path=DATASET_PATH, model_config=config_file, verbose = False)
end_time = time.time()
print("Total time to train model: " + str(end_time - start_time) + " seconds")

# Observe data preview
df = pd.read_csv(gretel.get_model().get_artifact_link("data_preview"), compression="gzip")
print(df)

# Get report URL
report_url = gretel.get_model().get_artifact_link("report")
print("Report URL: " + str(report_url))
