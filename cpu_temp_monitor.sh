#!/bin/bash

while true; do 

	temp_raw=$(cat /sys/class/thermal/thermal_zone0/temp)
	
	temp_c=$(echo "scale=2; $temp_raw / 1000"|bc)

	echo "$(date '+%Y-%m-%d %H:%M:%S') CPU temp:$temp_c C "

	sleep 1
done
