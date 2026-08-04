"""Cloud model factories shared by notebooks and applications."""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_chat_model(model: str | None = None) -> ChatOpenAI:
    """Create a LangChain chat model backed by the OpenAI API."""

    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY in .env before creating the model")

    return ChatOpenAI(
        model=model or os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),
        temperature=0,
    )
