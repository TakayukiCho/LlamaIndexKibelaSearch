# これは何？

Llama Indexを使ってWEBにある記事をベースに解答を作成するやつ。
個人実験用。

# 使い方

1. `$ brew install pipenv`
1. `$ pipenv install`
1. tmp/article-urls.csv に CSV形式で検索元の記事として利用したい記事のURLを貼りつけます
1. `$ touch .env OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}` 
1. `$ pipenv run python src/create_index.py`
1. `$ pipenv run python src/query.py`
