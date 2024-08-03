# OAuth2.0に必要なライブラリです。
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery



"""
クライアントシークレットのパスです。
本番環境では危険なので、環境変数か、.envを使って取得してください。
今回はテスト環境なので、ハードコードします。
例

import os
CLIENT_SECRETS_FILE = os.environ.get("CLIENT_SECRETS_FILE")
"""
CLIENT_SECRETS_FILE = "client_secret.json"


