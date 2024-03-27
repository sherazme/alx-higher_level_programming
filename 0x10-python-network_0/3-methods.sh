#!/bin/bash
# script that send request and deplay all HTTP allowed methods.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
