@echo off
setlocal

cd /d "%~dp0"
set "PORT=4173"
set "URL=http://127.0.0.1:%PORT%/index.html?mode=presenter#home"

where py >nul 2>&1
if not errorlevel 1 (
    set "PYTHON=py"
    goto :launch
)

where python >nul 2>&1
if not errorlevel 1 (
    set "PYTHON=python"
    goto :launch
)

echo Python was not found on PATH.
echo Install Python 3, then double-click this file again.
pause
exit /b 1

:launch
title Group10 PA4 Prototype Server
echo Starting Group10 PA4 prototype at %URL%
start "" "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Milliseconds 800; Start-Process '%URL%'"
%PYTHON% -m http.server %PORT%

