# **Python用 Google OAuth2.0非公式デモ**

#**Google OAuth2.0のデモサンプル**
初心者向けにOAuth2.0の実装例をFlaskで作ってみました。
独学で作ったので、もしかしたらもっといい作り方があるとは思いますが、なにかあればプルリクください(笑)。
#**使い方**
```
git clone https://github.com/DigiLog-lab/Google_OAuth2.0_Demo.git
```
をCLIで叩くだけで使えます。

依存関係のインストールは、
```
pip install -r requirements.txt
```
でできます。

サーバーを起動するには、
```
python3 main.py
```
で起動できます。

#**改変**
改変については、OAuth2.0のクライアントライブラリの規約に違反しなければいくらでもしてもらって大丈夫です。
ただ、このアプリをベースに新しくアプリを開発するのは、セキュリティー的にもおすすめしません。

#**役に立つリファレンス**

   [ウェブサーバー アプリケーションに OAuth 2.0 を使用する](https://developers.google.com/identity/protocols/oauth2/web-server?hl=ja#python_5)
