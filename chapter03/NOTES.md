# Chapter 03 Notes

> 以下の実行結果は、クラウドAPIへ移行する前に行ったLM Studio検証の記録です。
> 現在のNotebookは原本準拠のOpenAI API版へ戻しており、APIキー設定後に再実行します。

## 目標

- プロンプトエンジニアリングの役割を説明できる
- プロンプトをテンプレート化できる
- 出力形式を指示できる
- Zero-shotとFew-shotを使い分けられる
- Zero-shot Chain-of-Thoughtの効果を比較できる

## 学んだこと

- 指示なしの回答は約2,100文字まで広がったが、systemメッセージで「100文字程度」と
  指定すると約100文字に収まった。
- 入力をテンプレートへ埋め込む方法と、system/userメッセージへ役割を分ける方法の
  どちらでもレシピを生成できた。
- 出力形式をJSONとして例示すると、指定した`材料`と`手順`の構造で回答した。
- Zero-shotの感情分類では`ポジティブ`、通常のFew-shot分類では`true`を返した。
- 単純な計算では、直接回答とZero-shot Chain-of-Thoughtのどちらも正解は`8`だった。
  後者では途中計算が明示された。

## 実装上の判断

- 原本の26セルと実行順を維持する。
- Colab Secretsの代わりにルートの`.env`を使用する。
- Notebook内では`pip install`せず、`pyproject.toml`と`uv.lock`の環境を使用する。
- OpenAI SDKはLM StudioのOpenAI互換APIへ接続する。
- Completions APIの分類例は、反復を防ぐため出力を1行・10トークン以内に制限する。

## fastモデルで動いた機能

- systemメッセージによる回答長の制御
- プロンプトのテンプレート化
- 出力形式の指定
- Zero-shot分類
- user/assistantメッセージによるFew-shot分類
- Completions APIによるFew-shot形式
- Zero-shot Chain-of-Thought

## 原本との差と観察

- JSON形式の回答はMarkdownコードフェンス付きだった。厳密なJSONとして扱う場合は、
  第2章と同様にJSON Schemaを使うか、コードフェンスを除去する必要がある。
- Completions APIの分類結果は`true`だけではなく`A: true`になった。
- `system`メッセージの`name`に`example_user`と`example_assistant`を指定する
  Few-shot形式では、Gemmaは`true`ではなく説明文を返した。
- 今回の算術問題はZero-shotでも正解したため、Chain-of-Thoughtによる正答率の改善までは
  比較できず、回答過程の違いだけを確認した。

## strongモデルとの比較

## 次に確認すること

- 100文字制約が別の質問でも守られるか確認する。
- Few-shotの例を増減し、出力形式の安定性を比較する。
- Zero-shotでは間違えやすい問題を使い、Chain-of-Thoughtの効果を比較する。
