#!/bin/bash

# clean the build enviroment
rm -rf dist/
rm -rf build/

# activate the virtual enviroment
source .venv/bin/activate

# export the needed packages
pip3 freeze > requirements.txt

pyinstaller norsevpn.spec \
--onefile \
--noconsole \
--icon=doc/img/logo/norsevpn.ico \
--add-data="README.md:." \
--add-data="vizu/norsevpn.ui:." \
--add-data="vizu/config.ui:." \
--add-data="vizu/info.ui:." \
--paths ./vizu