"""Check the LM Studio server and print model identifiers available to the API."""

import os
import sys

from dotenv import load_dotenv
from openai import APIConnectionError, OpenAI


def main() -> int:
    load_dotenv()
    base_url = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
    client = OpenAI(
        base_url=base_url,
        api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    )

    try:
        models = sorted(model.id for model in client.models.list().data)
    except APIConnectionError:
        print(f"Could not connect to LM Studio at {base_url}", file=sys.stderr)
        print("Start the server in LM Studio's Developer tab and try again.", file=sys.stderr)
        return 1

    print(f"Connected to LM Studio at {base_url}")
    if not models:
        print("No models are currently visible to the API.")
        return 0

    print("Available model IDs:")
    for model in models:
        print(f"- {model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
