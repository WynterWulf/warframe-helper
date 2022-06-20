import requests
import urllib
import re

robots = "https://overframe.gg/robots.txt"

sitemap_ls = []

with urllib.request.urlopen(robots) as stream:
    for line in urllib.request.urlopen(robots).read().decode("utf-8").split('\n'):
        if 'Sitemap'.lower() in line.lower():
            sitemap_url = re.findall(r' (https.*xml)', line)[0]
            sitemap_ls.append(sitemap_url)