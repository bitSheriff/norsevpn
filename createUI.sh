#!/bin/bash

# clean the build enviroment
rm -rf dist/
rm -rf build/

# activate the virtual enviroment
source .venv/bin/activate

# create python files of the ui files so they can be easier used as standalones
python3 -m PyQt5.uic.pyuic -x vizu/main.ui   -o vizu/mainUI.py
python3 -m PyQt5.uic.pyuic -x vizu/config.ui -o vizu/configUI.py
python3 -m PyQt5.uic.pyuic -x vizu/info.ui   -o vizu/infoUI.py