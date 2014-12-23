#!/bin/bash
for path in Skripte/obrazi20/*;
do
	filename=$(basename $path);
	name=`echo $filename | cut -f1 -d'.'`
	./stasmMain -n 20 $path
	FILE="${name}_stasm.bmp"
	if [ -f $FILE ];
	then
		cp $FILE Skripte/obrazi20
		cp stasm.log Skripte/obrazi20/$name.log   
	fi
done