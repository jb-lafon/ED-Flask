# ==========
# File : scripts.py
# Author : Jb
# First created on : 24/10/2018
# Description: File for miscellaneous functions
# ==========

import requests
import re
from pyquery import PyQuery as Pq
from flask import request


def urlify(string):
    return string.replace(' ', '+')


def http_request(url):
    r = requests.get(url)
    data = r
    return data


def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def req_value(url):
    print("=======>>> Getting value...")
    page = http_request(url).text
    d = Pq(page)
    print("=======>>> Parsing...")
    bloc = d("div.panel>div.panel-body>p:last-of-type>strong")
    bloc = str(re.sub('&#13;', '', str(bloc)))
    bloc = str(re.sub('\n', '', bloc))
    if find_whole_word('estimated')(bloc):
        bloc = re.findall('(\d+)', bloc)  # Regex to select only digits
        bloc = ''.join(bloc)  # Join regex result to string
        value = int(bloc)
        print("=======>>> Valued parsed : "+str(value))
        return value
    else:
        print("=======>>> Valued not parsed...")
        return None


def appstop():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
