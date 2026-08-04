# agent-book-lab

『LangChainとLangGraphによるRAG・AIエージェント［実践］入門』を教材として、
クラウドAPIを使ったLangChain、LangGraph、RAG、AIエージェントを自分で実装しながら学ぶための
個人用リポジトリです。

このリポジトリには書籍の配布コードや原本Notebookを含めません。
原本はGit管理外の参照資料として保管し、内容を理解したうえで演習をゼロから実装します。

## 現在地

- [x] Python 3.11とuvによる実行環境
- [x] OpenAI／Tavily／LangSmith用の環境変数
- [x] 第2〜5章のクラウドAPI版Notebook
- [ ] APIキー設定後の全セル実行

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
クラウドAPIで検証する
  ↓
NOTES.mdへ記録する
```

## Setup

```bash
uv sync
cp .env.example .env
```

`.env`へ利用するサービスのAPIキーを設定します。`.env`はGit管理対象外です。

```dotenv
OPENAI_API_KEY=
TAVILY_API_KEY=
LANGSMITH_API_KEY=
```

LangSmithは任意です。`LANGSMITH_API_KEY`が空の場合、Notebookはトレースを無効にして実行します。

## Cloud models

| 役割 | 環境変数 | 現在のモデル |
|---|---|---|
| チャット | `OPENAI_CHAT_MODEL` | `gpt-4o-mini` |
| RAGの埋め込み | `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` |

```python
from agent_book.models import create_chat_model

model = create_chat_model()
```

## Checks

```bash
uv run ruff check .
uv run pytest
```

## Dependency policy

ルートの`pyproject.toml`と`uv.lock`で全章の依存関係を共有します。
Notebook内では`pip install`を実行しません。
