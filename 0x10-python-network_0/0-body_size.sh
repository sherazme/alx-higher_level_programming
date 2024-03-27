#!/bin/bash
# script that displays size of response body of given URL.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
