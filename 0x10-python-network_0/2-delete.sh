#!/bin/bash
# script that send delete request and seplay size of response body of given URL.
curl -s "$1" -X DELETE
