@Echo off
title INSTALL Running MneEthOn_V2.py Mmdrza.Com
Pushd "%~dp0"
pip install hdwallet
pip install lxml
pip install rich
pip install mnemonic
pip install requests_html
pip install --upgrade requests
:loop
python MneEthOn_V2.py
goto loop
