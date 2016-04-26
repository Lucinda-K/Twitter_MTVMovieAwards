#!/bin/bash

for file in ./Movie_of_Year/Avengers/*
do
	python textblob_practice.py "$file" >> creed.txt
done
