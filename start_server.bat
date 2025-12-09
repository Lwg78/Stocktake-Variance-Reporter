@echo off
title Stocktake Web Server
color 0B
echo ==========================================
echo      STARTING LOCAL WEB SERVER
echo ==========================================
echo.
echo 1. Keep this black window OPEN.
echo 2. Open your browser to: http://127.0.0.1:8000
echo.
uvicorn api:app --reload
pause