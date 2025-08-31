@echo off
setlocal

:: Step 0 - Shell compatibility notice
echo [INFO] This script is designed for Windows Command Prompt (cmd).
echo        Please do not run it in PowerShell or Git Bash.
echo.

:: Step 1 - Check if conda is available
where conda >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Conda not found. Please install Anaconda or Miniconda first.
    pause
    exit /b
)

:: Step 2 - Check if environment exists
conda info --envs | findstr /i "netflix_env" >nul
if errorlevel 1 (
    echo [INFO] Environment 'netflix_env' not found. Creating it from environment.yml...
    conda env create -f environment.yml
)

:: Step 3 - Activate environment
call conda activate netflix_env
if errorlevel 1 (
    echo [ERROR] Failed to activate environment. Try running: conda init cmd.exe
    pause
    exit /b
)

:: Step 4 - Check for required packages
echo [INFO] Verifying required packages...

python -c "import flask" 2>nul
if errorlevel 1 (
    echo [INFO] Flask not found. Installing...
    pip install flask
)

python -c "import pandas" 2>nul
if errorlevel 1 (
    echo [INFO] Pandas not found. Installing...
    pip install pandas
)

python -c "import plotly" 2>nul
if errorlevel 1 (
    echo [INFO] Plotly not found. Installing...
    pip install plotly
)

:: Step 5 - Launch dashboard
echo [INFO] Launching dashboard...
python app.py
if errorlevel 1 (
    echo [ERROR] Failed to launch Flask. Please check app.py and dependencies.
    pause
    exit /b
)

:: Step 6 - Success message
echo [SUCCESS] Dashboard is running at http://127.0.0.1:5000
echo [INFO] Press Ctrl+C to stop the server.
pause
