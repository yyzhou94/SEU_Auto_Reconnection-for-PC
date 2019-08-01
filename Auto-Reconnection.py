#!/usr/bin/env python
# -*- coding: utf-8 -*-
# code by: Yyzhou 2019-08-01
import urllib.request
import time
import socket


def http_validate(target_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} # 由于B站和QQ禁止爬虫，所以要加上头部
    req = urllib.request.Request(url=target_url, headers=headers)
    try:
        urllib.request.urlopen(req)  # 尝试访问网页
        if urllib.request.urlopen(req).getcode() == 200:  # 网页状态码为200
            return 1
        else:
            return 0
    except:    # 无法正常访问时也返回0
        return 0


def get_host_ip():  # 获取本机真实IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


class Vpn:
    def __init__(self, params):
        self.url = {
             'urlLogin': 'http://202.119.25.2:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C'+params['user']+'&user_password='+params['pwd']+'&wlan_user_ip='+get_host_ip()+'&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=jlh_me60&jsVersion = 3.3.2&v=3497'
        }

    def login(self):
        r = urllib.request.Request(self.url['urlLogin'])
        res = urllib.request.urlopen(r, timeout=20).read()
        return res


if __name__ == '__main__':
    user_account = {
        'user': '你的卡号',
        'pwd': '你的密码'
    }
    url1 = 'https://www.bilibili.com/'
    url2 = 'https://www.qq.com/'
    while True:
        if http_validate(url1) and http_validate(url2):
            print("鬼刀一开，走位走位，看不见，手里干，欸，难受~~~~~~")
            time.sleep(300)
        else:
            print("哇槽，包租婆，怎么没网啦！快给我重连！！！！！！！")
            vpn = Vpn(user_account)
            print("我的大刀早已饥渴难耐，赶快去BiliBili看鬼畜！！！！")
            result = vpn.login()
            print(result)
