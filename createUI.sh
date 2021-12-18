#!/bin/bash

# activate the virtual enviroment
echo " <---- Entering python virtual enviroment ----> "
source .venv/bin/activate

# create resources file
echo "Creating resources"
pyrcc5 vizu/vizu_resources.qrc -o vizu/vizu_resources.py

# create python files of the ui files so they can be easier used as standalones
echo "Create python file from the Qt ui files"
pyuic5 -x vizu/main.ui   -o vizu/mainUI.py
pyuic5 -x vizu/config.ui -o vizu/configUI.py
pyuic5 -x vizu/info.ui   -o vizu/infoUI.py

echo " <--- Exit vitual enviroment ----> "
exit