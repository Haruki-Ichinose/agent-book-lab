# Chapter 02 Notes

> 以下の実行結果は、クラウドAPIへ移行する前に行ったLM Studio検証の記録です。
> 現在のNotebookは原本準拠のOpenAI API版へ戻しており、APIキー設定後に再実行します。

## 目標

- 通常のチャット
- 会話履歴
- ストリーミング
- JSON出力
- 画像入力
- Function calling

## 学んだこと

- 原本の学習順は、トークン、通常の応答、会話履歴、ストリーミング、JSON、
  Vision、Completions API、Function calling。
- `tiktoken.encoding_for_model("gpt-4o")` では `ChatGPT` は2トークンに分かれ、
  原本の日本語サンプルは37トークンになる。
- `tiktoken` の結果はOpenAIモデル向けであり、Gemmaの実際のトークン数とは一致しない。

## 実装上の判断

- 原本の36セルと実行順を維持し、OpenAI SDKをLM StudioのOpenAI互換APIへ接続した。
- Colab Secretsの代わりにルートの`.env`を使用する。
- Notebook内では`pip install`せず、`pyproject.toml`と`uv.lock`の環境を使用する。
- Vision用の表紙画像は`chapter02/assets/cover.jpg`へ置き、Base64 Data URLに変換する。
- 原本の`json_object`は現在のLM Studioで受け付けられないため、JSON Schemaを使用する。

## fastモデルで動いた機能

- 通常のチャット
- 会話履歴
- ストリーミング
- JSON Schemaによる構造化出力
- ローカル画像を使ったVision
- Completions API
- Function calling

## 動かなかった機能と原因

- `response_format={"type": "json_object"}`: 現在のLM Studioは`json_schema`または`text`を要求する。
- リモート画像URLの直接指定: 現在のLM StudioはBase64エンコード画像を要求する。

## strongモデルとの比較

## 次に確認すること

- 2.3のトークンと文字数の違いを、自分で例文を変えて確認する。
- Completions APIで同じ文が反復された理由をChat Completions APIとの違いから考える。
- Function callingで`unit`が省略されると`null`になる実装を改善する。
