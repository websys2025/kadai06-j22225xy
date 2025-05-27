# 機能: 指定した統計表ID(statsDataId)の統計データを取得し、JSON形式で出力する
# 使い方: statsDataId を必要な統計表IDに変更して実行
import requests
import json

# --- 設定 ---
APPID = "bafe75ee2c8d2df315c37013b07735f083d5c7fe" 
# 今回取得する統計表IDの例: 0003211073 （都道府県別・法人企業数）
statsDataId = "0003211073"

# --- パラメータ設定 ---
params = {
    'appId': APPID,
    'statsDataId': statsDataId,
    'metaGetFlg': 'Y',    # メタ情報を取得
    'cntGetFlg': 'Y',     # 件数情報を取得
    'sectionHeaderFlg': '1'
}

# --- API 呼び出し ---
endpoint = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
response = requests.get(endpoint, params=params)

# ステータスコード確認
if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    exit(1)

# JSON パース
data = response.json()

# 結果表示
print(json.dumps(data, ensure_ascii=False, indent=2))