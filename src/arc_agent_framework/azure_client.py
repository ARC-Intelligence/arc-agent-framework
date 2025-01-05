# clients.py
import os

import dotenv
from langfuse.openai import AzureOpenAI

ENV_VARS_AZURE_OPENAI = {
    "4O": ("AZURE_4O_KEY", "AZURE_4O_VERSION", "AZURE_4O_ENDPOINT"),
    "4O_mini": ("AZURE_4O_MINI_KEY", "AZURE_4O_MINI_VERSION", "AZURE_4O_MINI_ENDPOINT"),
    "35": ("AZURE_35_KEY", "AZURE_35_VERSION", "AZURE_35_ENDPOINT"),
}


def _check_env_vars(model: str, env_keys: tuple) -> None:
    """Ensure all required environment variables for the given model are set."""
    missing = [key for key in env_keys if not os.getenv(key)]
    if missing:
        missing_str = "\n".join(missing)
        raise ValueError(
            f"""
            Azure environment variables not set for model '{model}'.
            Missing environment variables:
            {missing_str}
            """
        )


# Initialize and wrap the AzureOpenAI client
def get_client(model: str = "4O") -> AzureOpenAI:
    """Initialize and return an AzureOpenAI client for the specified model."""
    dotenv.load_dotenv()

    if model not in ENV_VARS_AZURE_OPENAI:
        raise ValueError(f"Invalid model name '{model}'. Must be one of {list(ENV_VARS_AZURE_OPENAI.keys())}.")

    # Check required environment variables
    required_envs = ENV_VARS_AZURE_OPENAI[model]
    _check_env_vars(model, required_envs)

    # Build the client using the validated environment variables
    api_key, api_version, azure_endpoint = (os.getenv(var) for var in required_envs)
    return AzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
    )


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
