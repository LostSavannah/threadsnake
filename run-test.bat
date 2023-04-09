if exist dist rd /s /q dist
py -m build
set ENVIRONMENT_NAME=testenv
py -m venv %ENVIRONMENT_NAME%
call %ENVIRONMENT_NAME%\Scripts\activate
for /f "delims=" %%i in ('dir /b ".\dist\*.whl"') do pip install .\dist\%%i
pip install requests
pip install pytest
pytest
deactivate
