import pytest

from agent_book.models import create_chat_model


def test_requires_openai_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "")

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        create_chat_model()


def test_uses_configured_default_model(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")

    model = create_chat_model()

    assert model.model_name == "gpt-4o-mini"


def test_accepts_explicit_model(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    model = create_chat_model("gpt-4o")

    assert model.model_name == "gpt-4o"
