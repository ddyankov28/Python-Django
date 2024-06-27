#!/bin/bash

# This is the bitly shortened github location of this exercise
# https://bit.ly/3S3Swgv

if [ "$#" -ne 1 ]
then
    echo "Error: Use 1 argument (the bit.ly shortened version)"
    exit 1
fi

if [ -z "$1" ]
then
    echo "Error: The argument is empty or not provided"
    exit 1
fi

curl --silent --head "$1" | grep "HTTP" > status_code.txt
status_code=$(cut -d " " -f 2 status_code.txt)

if [ "$status_code" != "301" ]
then
     echo "Error: Invalid bit.ly shortened address"
     rm -f status_code.txt
     exit 1
fi

curl --silent --head $1 | grep "location" > real_address.txt
real_location=$(cut -d " " -f 2 real_address.txt)
echo "$real_location"
rm -f status_code.txt
rm -f real_address.txt
 


### --- CURL ---- ###
#   Client URL (cURL) enables data exchange between a device and a server

# resources
# - https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/
# - https://www.baeldung.com/linux/curl-get-http-status#:~:text=Using%20%E2%80%93write%2Dout%20Option,to%20specify%20the%20output%20format.
# - https://www.geeksforgeeks.org/cut-command-linux-examples/