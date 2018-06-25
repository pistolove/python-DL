#!/user/bin/env python
# -*- coding: utf-8 -*-

# import webbrowser
#
# webbrowser.open('http://inventwithpython.com/')

import requests

headers = {'Accept': 'application/json',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Cookie': '_lxsdk_cuid=1632e00a85ac8-0cce31246f5fe9-6b1b1279-100200-1632e00a85b26; ci=1; oc=J9AcLJi3PK0hqQTEipUNkU27XshGrP-ku7X6zCTTAULE6y63HYGbXVPVgSQ-RcXP_mgnjjd3YjnNTIsRgQmWHsp5XVGrR1S7UXTTuBv0Xkv2nwdBy5120pZ7BtHhXDkwJO5ey_ECYq-DYnQGvKRXvypCFgq5GjyQsHRflSrlNvQ; __mta=255753527.1525485185346.1525485432064.1525489128194.5; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=1632e00a85ac8-0cce31246f5fe9-6b1b1279-100200-1632e00a85b26; lat=39.91103; lng=116.11028; uuid=585cc62de12445e0b4b6.1529937144.1.0.0; _lxsdk_s=164375e431b-82e-b06-977%7C%7C15; client-id=71046a26-77f9-4e4b-b633-cb980e11703f',
           'Host': 'www.meituan.com',
           'Referer': 'http://www.meituan.com/meishi/5103688/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

fs = open("F://shenghuo_meishi_body_url.list", "r")
for line in fs.readlines():
    if not line:
        continue
    line = line.strip()
    res = requests.get(line, headers=headers)
    print line, res.text
