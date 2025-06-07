# 勤怠マネージャー

出勤・退勤時刻を記録し、管理するアプリケーションです。

## セットアップ

1.  リポジトリをクローンします。
2.  仮想環境を作成し、アクティベートします。
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    # source venv/bin/activate
    ```
3.  必要なライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
4.  アプリケーションを実行します。
    ```bash
    flask run
    ```

## データベース

SQLiteを使用しています。初回実行時に `data/attendance.db` が作成されます。
