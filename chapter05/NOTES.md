# Chapter 05 Notes

## 目標

- RunnableとRunnableSequenceを理解する
- `invoke`、`stream`、`batch`を使い分ける
- RunnableLambdaでPython関数をChainへ組み込む
- RunnableParallelで複数のChainを並列実行する
- RunnablePassthroughで入力を後段へ引き渡す
- `astream_events`でChain内部のイベントを観察する
- SQLChatMessageHistoryで会話履歴を保持する

## 実装上の判断

- 原本の65セルと実行順を維持する。
- Colab Secretsの代わりにルートの`.env`を使用する。
- Notebook内では`pip install`せず、`pyproject.toml`と`uv.lock`の環境を使用する。
- Chat modelは原本どおりOpenAI APIの`gpt-4o-mini`を使用する。
- 検索は原本どおりTavily APIを使用する。
- LangSmithは`LANGSMITH_API_KEY`が設定されている場合だけ有効にする。

## 実行状況

APIキー設定後に全セルを実行する。

## 次に確認すること

- `invoke`、`stream`、`batch`の出力と実行時間の違い
- RunnableParallelの並列実行結果
- Tavily Retrieverから最終回答までのデータフロー
- `astream_events`で取得できるイベントの順序
- セッションIDごとに会話履歴が分離されること
