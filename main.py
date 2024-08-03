# OAuth2.0に必要なライブラリです。
import google_auth_oauthlib.flow


from flask import Flask, render_template, session, url_for, redirect, request

import os

"""
表記について
「URI」の名前を持つメソッドが出てくると思いますが、
便宜上「URL」と置き換えます。「URI」と書かれたメソッドが出てくると思いますが、
その際は「URL」と読み替えてください。
"""

"""
クライアントシークレットのパスです。
本番環境では危険なので、環境変数か、.envを使って取得してください。
今回はテスト環境なので、ハードコードします。
例
CLIENT_SECRETS_FILE = os.environ.get("CLIENT_SECRETS_FILE")
"""
CLIENT_SECRETS_FILE = "client_secret.json"

# スコープ(リクエストする権限のことです。)
# 今回はDriveAPIのスコープをリクエストします。
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

app = Flask(__name__)
app.secret_key = os.urandom(64)


"""
ログインが終わった後に表示されるページです。
"""
@app.route("/")
def home():
    message = "ログインに成功しました。"
    return message


@app.route("/login")
def login():
    """
    flowオブジェクトを作成します。
    OAuth2.0を行う上で、その流れを管理してくれるオブジェクトです。
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES
    )
    """
    認証を終えた後にリダイレクトするURLを設定します。
    """

    flow.redirect_uri = url_for("callback", _external=True)

    """
    ユーザーに認証ページにリダイレクトするためのURLを取得します。
    このURLにアクセスすると、よく見るGoogleの認証ページにリダイレクトされます。
    """
    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )
    """
    セッションにstateを保存します。
    このstateは、認証が終わった後に、
    リクエストが正しいかどうかを確認するためのものです。
    主にCSRF攻撃を防いだり、途中でのエラーなどを検知するために使われます。
    """
    session["state"] = state

    # ユーザーを認証ページにリダイレクトします。
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    """
    リクエストが正しいかどうか、stateを参照し確認を行います。
    そして、またflowオブジェクトを作成し、
    サーバーが認可サーバーに対して、トークンをリクエストする準備をします。
    """
    state = session["state"]
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES, state=state
    )
    flow.redirect_uri = url_for("callback", _external=True)
    authorization_response = request.url
    """
    ここでアクセストークンを取得し、セッションに保存します。
    """
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    session["credentials"] = credentials_to_dict(credentials)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    """
    セッションを削除し、ログアウトします。
    """
    session.clear()
    return redirect(url_for("login"))

"""
credentialsオブジェクトを辞書型に変換します。
"""
def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

if __name__ == "__main__":
    # httpでGoogle OAtuthが使えるようにするための変数を設定
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # デバッグモードを有効にして、アプリケーションを起動
    app.run(debug=True, host="localhost", port=4040)    