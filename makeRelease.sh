#!/bin/bash

# activate the virtual enviroment
source .venve/bin/activate

# export the needed packages
pip3 freeze > requirements.txt