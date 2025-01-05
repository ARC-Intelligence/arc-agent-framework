# clients.py
import os

import dotenv
from langfuse.openai import AzureOpenAI


# Initialize and wrap the AzureOpenAI client
def get_client(model="4O"):
    # Load environment variables
    dotenv.load_dotenv()
    # check if the model is valid
    if model not in ["4O", "4O_mini", "35"]:
        raise ValueError("Invalid model name")
    
    # check if the environment variables are set
    if model == "4O":
        if not os.getenv("AZURE_4O_KEY") or not os.getenv("AZURE_4O_VERSION") or not os.getenv("AZURE_4O_ENDPOINT"):
            raise ValueError(f"""
                             Azure environment variables not set. 
                             Available environment variables for model 4O are:
                             {os.getenv("AZURE_4O_KEY")}
                                {os.getenv("AZURE_4O_VERSION")}
                                {os.getenv("AZURE_4O_ENDPOINT")}
                             
                             """)
    elif model == "4O_mini":
        if not os.getenv("AZURE_4O_MINI_KEY") or not os.getenv("AZURE_4O_MINI_VERSION") or not os.getenv(
                "AZURE_4O_MINI_ENDPOINT"):
            raise ValueError(f"""
                             Azure environment variables not set. 
                             Available environment variables for model 4O_mini are:
                             {os.getenv("AZURE_4O_MINI_KEY")}
                                {os.getenv("AZURE_4O_MINI_VERSION")}
                                {os.getenv("AZURE_4O_MINI_ENDPOINT")}
                             
                             """)
    elif model == "35":
        if not os.getenv("AZURE_35_KEY") or not os.getenv("AZURE_35_VERSION") or not os.getenv("AZURE_35_ENDPOINT"):
            raise ValueError(f"""
                             Azure environment variables not set. 
                             Available environment variables for model 35 are:
                             {os.getenv("AZURE_35_KEY")}
                                {os.getenv("AZURE_35_VERSION")}
                                {os.getenv("AZURE_35_ENDPOINT")}
                             
                             """)

    if model == "4O":
        return AzureOpenAI(
            api_key=os.getenv("AZURE_4O_KEY"),
            api_version=os.getenv("AZURE_4O_VERSION"),
            azure_endpoint=os.getenv("AZURE_4O_ENDPOINT"),
        )
    elif model == "4O_mini":
        return AzureOpenAI(
            api_key=os.getenv("AZURE_4O_MINI_KEY"),
            api_version=os.getenv("AZURE_4O_MINI_VERSION"),
            azure_endpoint=os.getenv("AZURE_4O_MINI_ENDPOINT"),
        )
    elif model == "35":
        return AzureOpenAI(
            api_key=os.getenv("AZURE_35_KEY"),
            api_version=os.getenv("AZURE_35_VERSION"),
            azure_endpoint=os.getenv("AZURE_35_ENDPOINT"),
        )
    else:
        raise ValueError("Invalid model name")
    
    
def get_model_name(model):
    if model == "4O":
        return os.getenv("AZURE_MODEL_NAME_4O")
    elif model == "4O_mini":
        return os.getenv("AZURE_MODEL_NAME_4O_MINI")
    elif model == "35":
        return os.getenv("AZURE_MODEL_NAME_35")
    else:
        raise ValueError("Invalid model name")


wrapped_client = get_client("4O")  # Wrap the client for use in other modules


# Export the wrapped client for use in other modules
__all__ = ["wrapped_client"]
