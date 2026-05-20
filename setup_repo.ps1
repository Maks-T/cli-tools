# 4. Создаем .bat файл-обертку в папке bin (Динамический путь)
$BatFilePath = Join-Path $RepoPath "bin\ctools.bat"
$BatFileContent = @"
@echo off
REM Глобальная точка входа в меню (путь вычисляется автоматически)
python "%~dp0..\cli_menu.py" %*
"@
Set-Content -Path $BatFilePath -Value $BatFileContent -Encoding Default