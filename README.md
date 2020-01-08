# 英単語を日本語に訳して単語テストを作成するツール

## 使い方

- `git clone git@github.com:Kudoas/words_translater.git`でローカルにファイルをダウンロードする。

- ローカルのpython環境に`pip3 install googletrans`を入れるか`docker-compose up -d`で起動する環境を作る

- テスト作成用のファイルはtxt形式で`英単語のみ`か`1.	abide`のような形で一行ずつ用意する

```txt
例
apple
fish

1. apple
2. fish
```

- テスト作成用のファイルをenglish-wordsフォルダにwords.txtという名前で入れる

-  `python src/main.py`をコマンドに打つ

- outputに翻訳後のCSVファイルとtestfileに単語テストが自動生成される

## 注意点

- googletransの仕様で多数の英単語を翻訳するとリジェクトされる(デフォルトは100単語)
