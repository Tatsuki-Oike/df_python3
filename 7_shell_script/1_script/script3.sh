#!/bin/bash

sample_var="Hello"
sample_list=(1 2 3 4)

echo $sample_var
echo ${sample_list[0]}
echo ${sample_list[1]}
echo ${sample_list[2]}
echo ${sample_list[3]}
echo ${sample_list[@]}