@echo off
title NetflixDashboard Launcher

:: 檢查 Conda 是否安裝
where conda >nul 2>nul
if errorlevel 1 (
    echo ❌ 未偵測到 Conda，請先安裝 Anaconda 或 Miniconda。
    pause
    exit /b
)

:: 檢查環境是否已存在
conda info --envs | findstr netflix_env >nul
if errorlevel 0 (
    echo ✅ 環境已存在，跳過建立步驟。
) else (
    echo [1/4] 建立 conda 環境中...
    conda env create -f environment.yml
)

:: 啟用環境
echo [2/4] 啟用環境...
call conda activate netflix_env

:: 啟動 Flask dashboard
echo [3/4] 啟動 Flask dashboard...
python app.py

:: 結尾提示
echo [4/4] 完成！請在瀏覽器開啟 http://127.0.0.1:5000
pause
