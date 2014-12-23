#!/bin/bash
> files.list
for path in Skripte/obrazi/*;
do
	filename=$(basename $path);
	echo $filename  >> files.list
done