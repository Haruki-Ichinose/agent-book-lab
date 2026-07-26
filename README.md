# agent-book-lab

『LangChainとLangGraphによるRAG・AIエージェント［実践］入門』を教材として、
LM Studioを使ったLangChain、LangGraph、RAG、AIエージェントを自分で実装しながら学ぶための
個人用リポジトリです。

このリポジトリには書籍の配布コードや原本Notebookを含めません。
原本はGit管理外の参照資料として保管し、内容を理解したうえで演習をゼロから実装します。

## 現在地

- [x] Python 3.11とuvによるローカル環境
- [x] LM StudioのOpenAI互換APIへの接続
- [x] Gemma 4 E4Bによるチャット推論
- [x] EmbeddingGemmaによる日本語テキストの埋め込み生成
- [ ] 第2章のハンズオン

## 学習の進め方

各章では、自分で作るNotebookと学習記録を管理します。

```text
chapterXX/
├── notebook.ipynb  # 自分で実装するハンズオン
└── NOTES.md        # 学んだこと、失敗、モデル比較
```

```text
書籍と原本を読む
  ↓
目的とAPIを整理する
  ↓
自分で実装する
  ↓
fastモデルで検証する
  ↓
必要ならstrongモデルと比較する
  ↓
NOTES.mdへ記録する
```

## Setup

```bash
uv sync
cp .env.example .env
uv run python scripts/check_lmstudio.py
```

LM StudioのDeveloper画面でサーバーを起動し、`/v1/models`に表示されたモデルIDを
`.env`へ設定します。`.env`はGit管理対象外です。

## Models

| 役割 | 環境変数 | 現在のモデル |
|---|---|---|
| 日常的な開発 | `LM_STUDIO_FAST_MODEL` | `google/gemma-4-e4b` |
| 高精度な比較 | `LM_STUDIO_STRONG_MODEL` | `google/gemma-4-31b` |
| RAGの埋め込み | `LM_STUDIO_EMBEDDING_MODEL` | `text-embedding-embeddinggemma-300m` |

```python
from agent_book.models import create_chat_model

fast_model = create_chat_model("fast")
strong_model = create_chat_model("strong")
```

## Checks

```bash
uv run ruff check .
uv run pytest
```

## Dependency policy

ルートの`pyproject.toml`と`uv.lock`は、全章で共有する最小環境です。
RAG、ベクトルストア、評価ツールなどの章固有依存は、必要になった時点で検証して追加します。
