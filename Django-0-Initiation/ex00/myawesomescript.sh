#!/bin/bash

# This is the bitly shortened github location of this exercise
# https://bit.ly/3S3Swgv

if [ "$#" -ne 1 ]
then
    echo "Error: Use 1 argument (the bit.ly shortened version)"
    exit 1
if [ curl -s $1 | wc -l > 2]
then
    echo "Yes"
fi
#curl -s $1 | grep -o "http[^\"]*"
 


### --- CURL ---- ###
#   Client URL (cURL) enables data exchange between a device and a server

# resources
# - https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/
# - 