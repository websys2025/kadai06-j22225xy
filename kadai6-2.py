# 概要: 国際宇宙ステーション(ISS)の現在位置（緯度・経度）をリアルタイムで取得する
# エンドポイント: http://api.open-notify.org/iss-now.json
# 機能: API にアクセスして ISS の位置情報を取得し、タイムスタンプと緯度・経度を表示
# 使い方: 特別な認証不要。スクリプトを実行するだけで最新データを取得可能
import requests

# --- エンドポイント ---
url = "http://api.open-notify.org/iss-now.json"

# --- API 呼び出し ---
response = requests.get(url)

# ステータスコード確認
if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    exit(1)

# JSON パース
data = response.json()

# データ抽出
timestamp = data.get('timestamp')
position = data.get('iss_position', {})
latitude = position.get('latitude')
longitude = position.get('longitude')

# 結果表示
print(f"タイムスタンプ: {timestamp}")
print(f"緯度: {latitude}")
print(f"経度: {longitude}")