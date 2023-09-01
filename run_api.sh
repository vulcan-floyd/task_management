#!/bin/bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export CONFIG_NAME=$1
export FILE_PATH=static/uploads/
PYTHONPATH=./ python app.py
