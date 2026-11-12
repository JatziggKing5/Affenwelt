@echo off
rem Doppelklick (Windows): startet das Spiel lokal und oeffnet den Browser
cd /d "%~dp0"
start "" cmd /c "timeout /t 4 >nul & start http://localhost:3000"
npx serve . -l 3000
pause
