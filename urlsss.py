# -*- coding:utf-8 -*-

import requests


def get_redirect_url():
    # 重定向前的链接
    url = "https://none.h5.xeknow.com/st/34lpxTQWy"
    # 请求头，这里我设置了浏览器代理
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/8394 MicroMessenger/7.0.8.1540(0x27000834) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}
    # 请求网页
    response = requests.get(url, headers=headers,verify=False)
    print(response.status_code)  # 打印响应的状态码
    print(response.url)  # 打印重定向后的网址
    # 返回重定向后的网址
    return response.url


if __name__ == '__main__':
    redirect_url = get_redirect_url()
