#!/usr/bin/python3
"""sends POST request given URL with email parameter and display body"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    e_mail = {"email": argv[2]}
    req = requests.post(url, data=e_mail)

    print(req.text)
