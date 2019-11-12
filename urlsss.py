# -*- coding:utf-8 -*-

import requests


requests.packages.urllib3.disable_warnings()
def get_redirect_url():
    # 重定向前的链接
    url = "https://none.h5.xeknow.com/st/34lpxTQWy"
    # 请求头，这里我设置了浏览器代理
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/8394 Micromessenger/7.0.8.1540(0x27000834) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}
    # 请求网页
    data = {}
    response = requests.get(url, headers=headers,allow_redirects=False,verify=False)

      # 打印响应的状态码

    new_url = response.headers["Location"]
    print("----第一次重定向地址---------")
    print(response.status_code)
    print(new_url)
    print("-----------------")
    # 返回重定向后的网址
    one_url(new_url)

def one_url(url):
    url = url
    headers= {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/8394 Micromessenger/7.0.8.1540(0x27000834) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}

    res = requests.get(url, headers=headers,allow_redirects=False,verify=False)
    new_url = res.headers["Location"]
    print("-----第二次重定向地址------")
    print(res.status_code)
    print(new_url)
    print("-----------")
    two_url(new_url)

def two_url(url):
    url = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/8394 Micromessenger/7.0.8.1540(0x27000834) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}

    res = requests.get(url, headers=headers, allow_redirects=False, verify=False)
    new_url = res.headers["Location"]
    print("-----第三次重定向地址------")
    print(res.status_code)
    print(new_url)
    print("-----------")
    three(new_url)

def three(url):
    url = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/8394 Micromessenger/7.0.8.1540(0x27000834) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}

    res = requests.get(url, headers=headers, allow_redirects=False, verify=False)
    new_url = res.headers["Location"]
    print("-----第四次重定向地址------")
    print(res.status_code)
    print(new_url)
    print("-----------")
    return new_url


if __name__ == '__main__':
    redirect_url = get_redirect_url()
