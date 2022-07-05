#!/bin/bash

directory=$1
extension=$2
count=0

for entry in "$directory"/*$extension
do 
filename=$(basename -- $entry) #obtains the basename
echo "${filename%.*}"
#do echo "$entry"
        count=$((count+1))
done

echo $count" files were found" >/dev/stderr
