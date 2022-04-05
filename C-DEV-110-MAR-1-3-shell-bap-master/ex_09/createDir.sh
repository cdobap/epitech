#!/bin/bash
for i in $(seq -f %02g $1)
do 
mkdir -p ex_$i
done