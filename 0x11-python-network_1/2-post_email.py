#!/usr/bin/python3
"""sends POST request including URL and email and display body"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    e_mail = {"email": argv[2]}
    data = urlencode(e_mail).encode("ascii")
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
