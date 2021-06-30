from datetime import datetime
from pprint import pp

import click
import requests

urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
    "http://httpbin.org/get?text=you",
    "http://httpbin.org/get?text=can",
    "http://httpbin.org/get?text=almost",
    "http://httpbin.org/get?text=do",
    "http://httpbin.org/get?text=anything",
    "http://httpbin.org/get?text=with",
    "http://httpbin.org/get?text=it",
] # 12 requests


def get_args(url):
    return requests.get(url).json()["args"]


start = datetime.now()
pp([get_args(url) for url in urls])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
