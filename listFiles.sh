#!/bin/bash
for path in jpegs/*;
do
	filename=$(basename $path);
	name=`echo $path | cut -f1 -d'.'`
	if [ -f "${name}.log" ] ;
	then
		echo "${name}.jpg"  >> ./filesTemp.list
	fi
done
awk '!x[$0]++' filesTemp.list > files.list  #remoes duplicates from file
rm -f filesTemp.list