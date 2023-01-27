#!/bin/bash

echo $#

if [ $# = 2 ] && [ $2 = "flag" ]; then
    python 7_shell_script/4_python/sample.py --arg1 $1 --arg2
else
    python 7_shell_script/4_python/sample.py --arg1 $1
fi