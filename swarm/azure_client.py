# clients.py
import os

import dotenv
from langfuse.openai import AzureOpenAI

# Load environment variables
dotenv.load_dotenv()


# Initialize and wrap the AzureOpenAI client
def get_client(model="4o"):
    if model == "4o":
        return AzureOpenAI(
            api_key=os.getenv("AZURE_4o_KEY"),
            api_version=os.getenv("AZURE_4o_VERSION"),
            azure_endpoint=os.getenv("AZURE_4o_ENDPOINT"),
        )
    elif model == "4o_mini":
        return AzureOpenAI(
            api_key=os.getenv("AZURE_4o_MINI_KEY"),
            api_version=os.getenv("AZURE_4o_MINI_VERSION"),
            azure_endpoint=os.getenv("AZURE_4o_MINI_ENDPOINT"),
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
    if model == "4o":
        return os.getenv("AZURE_MODEL_NAME_4O")
    elif model == "4o_mini":
        return os.getenv("AZURE_MODEL_NAME_4O_MINI")
    elif model == "35":
        return os.getenv("AZURE_MODEL_NAME_35")
    else:
        raise ValueError("Invalid model name")


wrapped_client = get_client("4o")  # Wrap the client for use in other modules


# Export the wrapped client for use in other modules
__all__ = ["wrapped_client"]
