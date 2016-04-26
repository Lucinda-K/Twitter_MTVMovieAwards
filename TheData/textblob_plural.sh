#!/bin/bash

let count=0

for file in ./$1/*
do
	data=$(python calculate.py "$file")
	echo $data
done

exit 0

