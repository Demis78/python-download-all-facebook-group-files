#!/usr/bin/env python
from __future__ import print_function
import json
import requests
import os
import os.path
import errno
import sys
import urllib

import facepy


def download_file(url):
    r = requests.get(url, stream=True)
    fileNameRaw = url.split('/')[-1]
    fileName = urllib.parse.unquote(fileNameRaw)

    with open(fileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
                f.flush()


def dl_fb_files(groupId, accessToken):
    graph = facepy.GraphAPI(accessToken)
    getString = '/v2.2/' + groupId + '/files'
    pages = graph.get(getString, page=True, retry=5, limit=2000)


    try:
        os.makedirs(groupId)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(groupId):
            pass
        else: raise

    os.chdir(os.path.join(os.getcwd(), groupId))


    for page in pages:
        for post in page['data']:
            url = post['download_link']
            print('fetching ' + url)
            download_file(url)


if __name__ == '__main__':
    if not len(sys.argv) > 2:
        print('Usage:')
        print('$ ./dl_fb_files.py GROUPID ACCESSTOKEN')
        sys.exit(1)

    dl_fb_files(sys.argv[1], sys.argv[2])

