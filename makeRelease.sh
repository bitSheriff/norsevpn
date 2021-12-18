#!/bin/bash

# clean the build enviroment
ehco "Delete old builds"
rm -rf dist/
rm -rf build/

# create new python files from ui
bash createUI.sh

# activate the virtual enviroment
echo " <---- Entering python virtual enviroment ----> "
source .venv/bin/activate

# export the needed packages
echo "Export needed packages"
pip3 freeze > requirements.txt

echo "Create the portable single execute file"
pyinstaller norsevpn.py \
--onefile \
--icon=doc/img/logo/norsevpn.ico \

echo " <--- Exit vitual enviroment ----> "
exit