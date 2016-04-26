#!/bin/bash

for file in ./Movie_of_Year/StarWars/*
do
	python textblob_practice.py "$file" >> results.out
done
