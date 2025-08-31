NetflixDashboard 是一個互動式資料視覺化平台，透過 Flask 與 Plotly 打造，將原始的 Netflix 資料轉化為易於探索的儀表板。使用者可以透過精心設計的圖表，深入了解不同類型、國家與評分的分佈趨勢。

方法一：手動啟動（適用於所有平台）

# 1. 下載專案
git clone https://github.com/EricFang530/NetflixDashboard.git
cd NetflixDashboard

# 2. 建立並啟動 Conda 環境
conda create -n netflixenv python=3.11
conda activate netflixenv

# 3. 安裝依賴套件
pip install -r requirements.txt

# 4. 執行應用程式
python app.py

啟動後請造訪 http://127.0.0.1:5000 以瀏覽儀表板。




