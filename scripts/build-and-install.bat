cd ..
pip3 uninstall -y threadsnake
py -m build
for /f "delims=" %%i in ('dir /b ".\dist\*.whl"') do pip3 install .\dist\%%i
cd scripts