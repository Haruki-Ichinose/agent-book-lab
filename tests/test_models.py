import pytest

from agent_book.models import create_chat_model


def test_rejects_unknown_profile() -> None:
    with pytest.raises(ValueError, match="Unknown model profile"):
        create_chat_model("unknown")


def test_requires_configured_model(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LM_STUDIO_FAST_MODEL", "")

    with pytest.raises(RuntimeError, match="LM_STUDIO_FAST_MODEL"):
        create_chat_model("fast")
