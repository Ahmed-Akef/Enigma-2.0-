@echo off
title Enigma 2.0 Launcher
color 0a
cls
echo ===================================================
echo           ENIGMA 2.0 SYSTEM LAUNCHER
echo ===================================================
echo.
echo [1/3] Checking environment...
py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python (py launcher) is not installed.
    pause
    exit
)

echo [2/3] Installing/Verifying dependencies...
py -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Warning: Could not install dependencies. Trying to run anyway...
)

echo [3/3] Initializing System...
echo.
echo Opening secure channel...
start http://127.0.0.1:5001
echo.
echo System Active. DO NOT CLOSE THIS WINDOW.
echo Press Ctrl+C to terminate the system.
echo.
py app.py
pause
