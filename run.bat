@echo off
title Stocktake Variance Reporter
color 0A

echo ========================================================
echo        AUTOMATED STOCKTAKE VARIANCE REPORTER
echo ========================================================
echo.
echo [Status] Checking for input files...
echo.

:: Run the Python script
python main.py

echo.
echo ========================================================
echo [Status] Job Complete.
echo Please check the 'output' folder for your report.
echo ========================================================
echo.
pause