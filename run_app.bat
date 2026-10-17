@echo off
setlocal enabledelayedexpansion
title Placement Readiness Data Explorer - Launcher

echo ======================================================================
echo           PLACEMENT READINESS DATA EXPLORER - LAUNCHER
echo ======================================================================
echo.

:: 1. Navigate to script directory reliably
cd /d "%~dp0"
echo [1/3] Working directory: %CD%

:: 2. Check for Python in system PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in your system PATH.
    echo Please install Python 3.8 or higher from python.org
    echo and ensure Add Python to PATH is checked during installation.
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
echo [2/3] Detected %PYTHON_VER%

:: 3. Check for virtual environment and activate if present
if exist "venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment: venv
    call "venv\Scripts\activate.bat"
) else if exist ".venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment: .venv
    call ".venv\Scripts\activate.bat"
)

:: 4. Verify required packages
python -c "import streamlit, pandas, numpy" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] Required packages streamlit, pandas, or numpy are missing.
    echo To install them, run:
    echo     pip install -r requirements.txt
    echo.
    set /p INSTALL_CHOICE="Would you like to install them now? [y/n]: "
    if /i "!INSTALL_CHOICE!"=="y" (
        echo [*] Installing dependencies from requirements.txt...
        python -m pip install -r requirements.txt
        if %errorlevel% neq 0 (
            echo [ERROR] Package installation failed. Please check your internet connection.
            pause
            exit /b 1
        )
    ) else (
        echo [INFO] Cannot start application without required packages.
        pause
        exit /b 1
    )
)

:: 5. Launch the Streamlit application
echo [3/3] Starting Streamlit web application...
echo.
echo ======================================================================
echo Application starting at: http://localhost:8501
echo Press Ctrl + C in this terminal window to stop the server.
echo ======================================================================
echo.

python -m streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Streamlit exited with an error code: %errorlevel%
    pause
)
