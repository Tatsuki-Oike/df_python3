#!/bin/bash

arg1=$1
arg2=$2

if [ $arg1 = "a" ]; then
    echo "a"
fi

if [ $arg1 = "a" ] || [ $arg2 = "b" ]; then
    echo "success or"
fi

if [ $arg1 = "a" ] && [ $arg2 = "b" ]; then
    echo "success and"
fi