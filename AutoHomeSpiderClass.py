#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2019/5/5
# @Author  : 圈圈烃
# @File    : AutoHomeSpiderClass
# @Description:
#
#
import requests
import re
import random


class AutoHomeSpider:

    def __init__(self):
        self.headers = {
            "Host": "club.autohome.com.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            # "Referer": "https://club.autohome.com.cn/bbs/forum-c-871-1.html",
            "Connection": "keep-alive",
            # "Cookie": "ahpvno=6; pvidchain=3311253,3311253,6826793; fvlid=1557020630617i73BVtciYK; sessionip=183.132.184.132; sessionid=B6D727B8-56B0-46DD-9140-B514F3B80337%7C%7C2019-05-05+09%3A43%3A50.886%7C%7C0; autoid=a0a8f7d79866d31f24be9bcf9724c23c; ref=0%7C0%7C0%7C0%7C2019-05-05+09%3A58%3A43.321%7C2019-05-05+09%3A43%3A50.886; sessionvid=6BE01EFE-8AC0-4E09-95CA-4E2E9BC9EE5B; area=330299; ahpau=1; csrfToken=VGKFGgbqfyaZYv04pi7q1A3U; historybbsName4=c-871%7C%E9%AB%98%E5%B0%94%E5%A4%AB; __ah_uuid_ng=u_76903609; ahrlid=1557020956401U1ZVKhrjn6-1557022506437",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
        }

    def get_html(self, url):
        # ipPools = requests.get('http://127.0.0.1:8899/api/v1/proxies', params={"anonymous": True})
        # ipNum = random.randint(0, len(ipPools.json()))
        # print(ipNum)
        # randomIP = ipPools.json()['proxies'][ipNum]['ip']
        # randomPort = ipPools.json()['proxies'][ipNum]['port']
        # res = requests.get('http://api.ipify.org', proxies={'http': 'http://%s:%s' % (randomIP, randomPort)}, timeout=5)
        res = requests.get(url, proxies={'http': 'http://94.16.120.18:5555'}, timeout=5)
        print(res.text)


def main():
    url = "https://club.autohome.com.cn/bbs/thread/a57a4ba8b2a2d824/80709874-1.html"
    auto = AutoHomeSpider()
    auto.get_html(url)


if __name__ == '__main__':
    main()
