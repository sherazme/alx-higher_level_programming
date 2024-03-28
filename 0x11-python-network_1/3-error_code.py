#!/usr/bin/python3
"""displays response body of taken URL (decoded in utf-8)"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
