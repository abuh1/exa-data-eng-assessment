@echo off
setlocal

rem Set the project directory and main source code directory
set project_dir=%cd%
set main_dir=src

rem Set the root directory in the Python path
set PYTHONPATH=%project_dir%\%main_dir%

rem Run the Python script
python -m %main_dir%

endlocal
goto :eof