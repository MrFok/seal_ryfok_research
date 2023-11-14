from gretel_client import create_project, get_project
from gretel_client.projects import Project, create_or_get_unique_project
from gretel_client.projects.models import read_model_config, Model
from gretel_client.helpers import poll
import pandas as pd
import sys
import json

class GretelACTGAN:
    def __init__(self, project_name:str):
        """
        Creates a GretelACTGAN object.

        One of Gretel's main models, ACTGAN is an adversarial model that is the fastest 
        and most efficient model they have for generating tabular data. It is based on 
        the CTGAN model. 

        Gretel's documentation: https://docs.gretel.ai/reference/synthetics/models/gretel-actgan
        CTGAN paper: https://arxiv.org/abs/1907.00503

        Args:
            project_name (str): The name of the project to create or retrieve.
        """
        self.project_name = project_name
        self.project = create_or_get_unique_project(name=project_name)
        self.dataset_path = None
        self.config = None
        self.model = None
        self.generation_number = 0
    
    def create_config(self, model_config:str = "synthetics/tabular-actgan", epochs: str = "auto", num_records: int = 5000, \
                      dp: bool = False, outliers: str = None, similarity: str = "None", overfit: bool = False, verbose: bool = True):
        """
        Creates a configuration for the GretelProject object.
        
        Args:
        - model_config (str): The path to the model configuration file. Default is "synthetics/tabular-actgan".
        - epochs (str): The number of epochs to train the model. Default is "auto".
        - num_records (int): The number of records to generate. Default is 5000.
        - dp (bool): Whether to use differential privacy. Default is False.
        - outliers (str): The outlier filter to use. Must be either "auto", "medium", or "high". Default is None.
        - similarity (str): The similarity filter to use. Must be either "medium" or "high". Default is "None".
        - overfit (bool): Whether to use overfitting protection. Default is False.

        Return:
        - config (dict): The configuration for the GretelProject object.
        """
        # if model_config is not None:
        #     try:
        #         self.config = read_model_config(model_config)
        #     except:
        #         print("Model configuration file not found. Please check the path and try again.")
        #         sys.exit(1)
        self.config = read_model_config(model_config)
        
        self.config["models"][0]["actgan"]["params"]["epochs"] = epochs
        self.config["models"][0]["actgan"]["generate"]["num_records"] = num_records

        # Differential Privacy (Experimental, based on Differentially-Private Stochastic Gradient Descent)
        self.config["models"][0]["actgan"]["privacy_filters"]["dp"] = dp

        # Outlier Filter ("auto", "medium", "high")
        if outliers is not None:
            if outliers != "auto" or outliers != "medium" or outliers != "high":
                raise ValueError("Outliers must be either 'auto', 'medium', or 'high'.")
            self.config["models"][0]["actgan"]["privacy_filters"]["outliers"] = outliers

        # Similarity Filter ("auto", "medium", "high")
        # if similarity is not None:
        #     if similarity != "medium" or similarity != "high" or similarity != "auto":
        #         raise ValueError("Similarity must be either 'medium' or 'high'.")

        self.config["models"][0]["actgan"]["privacy_filters"]["similarity"] = similarity

        # Overfitting Protection
        if overfit:
            self.config["models"][0]["actgan"]["privacy_filters"]["validation_split"] = True
            self.config["models"][0]["actgan"]["privacy_filters"]["early_stopping"] = True

        if not verbose:
            print(f"Model configuration:\n{json.dumps(self.config, indent=2)}")
        return self.config

    def generate_model(self, dataset_path: str = None, model_config:str = None, verbose: bool = True):
        """
        Generates a model object using the specified dataset path and model configuration.
        NOTE: This DOES NOT train the model. It only creates the model object. You will 
        still need to run train() to train the model.

        Args:
            dataset_path (str): The path to the dataset to be used for training the model.
            model_config (str): The configuration to be used for the model. If not specified, the method will check if a configuration
                                has already been created or specified. If not, it will raise a ValueError.

        Returns:
            model (Model): The model object created using the specified dataset path and model configuration.

        Raises:
            ValueError: If dataset_path is not specified or if model_config is not specified and no configuration has been created
                        or specified yet.
        """

        if dataset_path is None:
            raise ValueError("Dataset path was not specified. Please specify a dataset path.")
        
        if model_config is None:
            if self.config is None:
                raise ValueError("Model configuration created or specified. Please specify a model configuration in the parameter or \
                                  call create_config() first.")
        else:
            self.config = model_config
        
        self.model = self.project.create_model_obj(model_config=self.config, data_source=self.dataset_path)
        self.model.submit_cloud()

        if not verbose: 
            poll(self.model, verbose=False)
            print(f"Follow along with training in the console: {self.model.get_console_url()}")
            poll(self.model, verbose=False)

        return self.project.get_console_url()
        
    
    def retrieve_model(self, model_id: str = None):
        """
        Retrieves an existing model object from the project, or one generated by generate_model().

        Args:
            model_id (str): The ID of the model to retrieve. If not specified, the method will return the model object created by
                            generate_model().

        Returns:
            model (Model): The model object retrieved from the project.
        """
        if model_id is not None:
            self.model = self.project.get_model(model_id)       

        return self.model
    
    def get_model(self):
        """
        Retrieves the model ID

        Return:
            model (Model): The model object.
        """
        return self.model

    def generate_synthetic_data(self, num_records:int, max_invalid:int, verbose:bool = True, download:bool = False, \
                                output_path:str = "gretel\\data\\"):
        """
        Generates synthetic data using the model object
        NOTE: This implementation only submits the model for cloud training, not local training. 
        TODO: Implement the other ways to submit and train a model (hybrid and local)

        Args:
            num_records (int): The number of records to generate.
            max_invalid (int): The maximum number of invalid records to allow.
            verbose (bool): Whether to print the synthetic data. Default is False.
        
        Return:
            synthetic_df (pd.DataFrame): The synthetic data as a pandas dataframe.
        """        
        params = {"num_records": num_records, "max_invalid": max_invalid}
        record_handler = self.model.create_record_handler_obj(params=params)
        record_handler.submit_cloud()

        if not verbose:
            poll(record_handler, verbose=False)

        synthetic_df = pd.read_csv(record_handler.get_artifact_link("data"), compression="gzip")

        if not verbose:
            print(synthetic_df)

        if download:
            path = output_path + self.project_name + "_" + str(self.generation_number) + \
                "-" + f"{int(num_records):03d}" + "-" + f"{int(max_invalid):03d}"+ "_synthetic_data.csv"
            
            if not verbose:
                print("Downloading synthetic data to " + path)

            synthetic_df.to_csv(path, index=False)

            if not verbose:
                print("Done!")
        return synthetic_df
    
    # TODO: This function is broken. Tried downloading "report" & produced following error:
    # pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 7, saw 2
        
    # def download_csv_artifact(self, output_path: str = "GretelTest\\data", artifact:str = "data_preview", verbose: bool = True):
    #     """
    #     Downloads an artifact from the model object into the specified directory

    #     Args:
    #         output_path (str): The path to the directory where the artifact will be downloaded. Default is "GretelTest\\data".
    #         artifact (str): The artifact to retrieve. Default is "data_preview".
    #         Other valid artifacts are: 'model', 'report', 'report_json', 'classification_report',
    #                 'classification_report_json', 'regression_report', 'regression_report_json', 
    #                 'text_metrics_report', 'text_metrics_report_json', 'data_preview', 'model_logs'
    #         verbose (bool): Whether to print the synthetic data. Default is False.
        
    #     """
    #     synthetic_df = pd.read_csv(self.model.get_artifact_link(artifact), compression="gzip")
    #     path = output_path + self.project_name + "_" "model_preview.csv"
    #     synthetic_df.to_csv(path, index=False)
    #     if not verbose:
    #         print("Model preview downloaded to " + path)