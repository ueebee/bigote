## ヒゲ取りBotのサンプル実装


https://note.com/japaneseml/n/nc3bd17bc2b70

を拝見して、学習ネタとしてサンプル実装したコードです。

記事中にある「髭取り」というところから、codenameをヒゲガラのスペイン名bigoteとしています。


## 機能

- Binanceのwebsocketデータを取得してPostgreSQLへ保存
- 外部で取得したXAUUSDのデータを受け取りPostgreSQLへ保存


## 初期設定

docker環境前提です。
以下の手順でBinanceのデータ取得をwebsocket経由で行いPostgreSQLに保存します。

```
# ソースを落としてくる
$ git clonne https://github.com/ueebee/bigote.git
$ cd bigote

# app/.env.exampleをapp/.envにコピーしてBinanceのAPI KeyとSecretを書き換えてください。
$ cp app/.env.example app/.env

# 初回起動
$ docker-compose up -d 

# 初回起動時のみmigration流す
$ docker exec -it bigote-fetcher bash
# orator migrate -c migrations/config.yml

# 起動
docker-compose down && docker-compose up -d
```

# BinanceAPIからデータ取得

containerが起動すると、Binanceから以下のデータを取得してPGに保存します。

- paxgusdt@aggTrade
- paxgusdt@miniTicker
- paxgusdt@depth20@100ms

# 外部データの受け取り

外部から以下のデータを受け取りPGに保存するAPIサーバーを起動します。

```
curl -X 'POST' \
  'https://example.com:3000/currency_pair' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "time": 0,
  "bid": 0,
  "ask": 0,
  "last": 0,
  "volume": 0,
  "time_msc": 0
}'
```

