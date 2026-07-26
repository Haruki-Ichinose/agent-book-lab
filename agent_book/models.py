"""Model factories shared by the notebooks and applications."""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_chat_model(profile: str | None = None) -> ChatOpenAI:
    """Create a LangChain chat model backed by LM Studio.

    The base URL stays on localhost even when LM Link routes inference to a
    remote device. Only the model identifier needs to change.
    """

    load_dotenv()
    selected_profile = profile or os.getenv("MODEL_PROFILE", "fast")
    model_variables = {
        "fast": "LM_STUDIO_FAST_MODEL",
        "strong": "LM_STUDIO_STRONG_MODEL",
    }

    if selected_profile not in model_variables:
        choices = ", ".join(sorted(model_variables))
        raise ValueError(f"Unknown model profile {selected_profile!r}; choose one of: {choices}")

    model_variable = model_variables[selected_profile]
    model_name = os.getenv(model_variable)
    if not model_name:
        raise RuntimeError(f"Set {model_variable} in .env before creating the model")

    return ChatOpenAI(
        model=model_name,
        base_url=os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1"),
        api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
        temperature=0,
    )
