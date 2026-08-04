# Chapter 04 Notes

> 以下の実行結果は、クラウドAPIへ移行する前に行ったLM Studio検証の記録です。
> 現在のNotebookは原本準拠のOpenAI API版へ戻しており、APIキー設定後に再実行します。

## 目標

- LangChainのLLMとChat modelを使い分ける
- PromptTemplateとChatPromptTemplateを理解する
- Output parserでモデル出力をPythonオブジェクトへ変換する
- LCELでPrompt・Model・Parserを連鎖する
- Document loader、text splitter、Embedding、Vector storeを使う
- LCELで小さなRAG Chainを組み立てる

## 学んだこと

- `OpenAI`のLLMインターフェースは文字列を返し、`ChatOpenAI`はmessage履歴を扱う。
- `PromptTemplate`は文字列、`ChatPromptTemplate`はrole付きmessageを生成する。
- `MessagesPlaceholder`を使うと、会話履歴をPromptへ差し込める。
- `PydanticOutputParser`とJSON Schemaのどちらでも、モデル出力を`Recipe`へ変換できた。
- LCELの`|`でPrompt、Model、Output parserを順番に接続できた。
- GitLoaderで2文書を読み、Embedding、Chroma、Retriever、RAG Chainまで接続できた。

## 実装上の判断

- 原本の73セルと実行順を維持する。
- Colab Secretsの代わりにルートの`.env`を使用する。
- Notebook内では`pip install`せず、`pyproject.toml`と`uv.lock`の環境を使用する。
- LangSmithはAPIキーと明示的な有効化がある場合だけ使用する。
- Vision用画像は`chapter04/assets/cover.jpg`をBase64 Data URLへ変換する。
- 原本の`json_object`は現在のLM Studioで受け付けられないため、JSON Schemaを使用する。
- 原本の`.mdx`文書は現行LangChainリポジトリに存在しないため、S3 Document loaderの
  Python実装2ファイルだけをRAGデータとして使用する。
- EmbeddingはLM Studioの`LM_STUDIO_EMBEDDING_MODEL`を使用する。

## fastモデルで動いた機能

- LLMとChat model
- Chat modelのストリーミング
- PromptTemplate、ChatPromptTemplate、MessagesPlaceholder
- ローカル画像を使ったVision
- PydanticOutputParser、StrOutputParser
- LCELによるChain
- JSON Schemaによる構造化出力
- `with_structured_output`のJSON Schema方式
- GitLoader、CharacterTextSplitter
- EmbeddingGemmaによる768次元のEmbedding
- Chromaの類似検索
- Retrieverを組み込んだRAG Chain

## 原本との差と観察

- LangSmithは未設定のためトレースを送らず、Prompt Hubの例では同等のローカルPromptを使った。
- `OpenAI`のLLMインターフェースでは「こんにちは」が反復された。Chat modelでは自然な応答になった。
- 原本の`json_object`は現在のLM Studioで受け付けられないため、JSON Schemaを使用した。
- `with_structured_output`の既定Function callingは、LangChain 0.2.0がオブジェクト形式の
  `tool_choice`を送るためLM Studioで失敗した。`method="json_schema"`で同じ目的を実現した。
- 現行LangChainリポジトリには原本対象の`.mdx`文書がないため、commit
  `cdca311de2958e497cfd823a45ddb770d0ef94c0`のS3 loader実装2ファイルを使用した。
- 2文書は2チャンクになり、Retrieverは`S3DirectoryLoader`と`S3FileLoader`を取得した。
- 最終RAG回答は、S3用loaderとして上記2種類を文脈に基づいて回答した。

## strongモデルとの比較

## 次に確認すること

- LLMとChat modelで同じ入力を与え、応答品質とメタデータを比較する。
- chunk sizeとRetrieverの`k`を変え、検索結果を比較する。
- RAGの回答が文脈外の情報を加えていないか確認する。
- strongモデルで構造化出力と最終RAG回答を比較する。
