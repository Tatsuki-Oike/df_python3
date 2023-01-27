#!/bin/bash

for arg in 3 4 5
do
    if [ "$1" = "flag" ]; then
        python 7_shell_script/4_python/sample.py --arg1 $arg --arg2
    else
        python 7_shell_script/4_python/sample.py --arg1 $arg
    fi
done