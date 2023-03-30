# GPT-Discensor

GPT-Discensorは、Discordに送信されたメッセージをOpen　AIのAPIに送信し、日本語の会話の一部ではないと判断された場合、そのメッセージを削除します。



https://user-images.githubusercontent.com/113443658/228916707-3981cdb2-9049-4da4-a5a0-a022712dbc34.mov




## 動作確認済環境
- Apple M1 Macbook Air
- MacOS Ventura 13.1

## 使い方

### 1. リポジトリをクローンする

```bash 
git clone https://github.com/edojidaipj/GPT-Discensor.git
```


### 2. .envファイルを作成する

```bash
cp .env.example .env
```


### 3. DiscordにBotを追加する

1. [Discord Developer Portal](https://discord.com/developers/applications)にアクセスし、Discordアカウントでサインインします。 
2. 「新しいアプリケーション」ボタンをクリックし、アプリケーションに名前を付けます。 
3. 「Bot」タブに移動し、「Add Bot」ボタンをクリックして新しいボットを作成します。 
4. ボットのTOKENをコピーして、.envにペーストします。
5. 「OAuth2」タブに移動し、「bot」スコープを選択します。次に、「Manage Messages」権限を選択します。
6.  生成されたOAuth2 URLをコピーして、新しいブラウザタブに貼り付けます。ボットをDiscordサーバーに参加させます。
7. 「Bot」タブに移動し、Privileged Gateway Intents内のMESSAGE CONTENT INTENTを有効にし、Save Changesをクリックします。

### 4. Open AIのAPIキーを追加する

1. [こちら](https://platform.openai.com/account/api-keys)でCreate new secret keyをクリックしてAPIキーを作成します
2. 生成されたAPIキーをコピーして、.envにペーストします。

### 5. ローカルで実行する
    
Python3の仮想環境を作成する
```bash
python3 -m venv venv
```

Python3の仮想環境を有効にする
```bash
source venv/bin/activate
```

コードの実行に必要なライブラリをインストールする
```bash
pip install -r requirements.txt
```

コードを実行する（サーバーを監視している間は実行したままにしておいて下さい）
```bash
python3 main.py
```


### 6. 停止する
    
```bash
Ctrl + C
```
