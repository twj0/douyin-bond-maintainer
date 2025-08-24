import os
import json
import random

def get_config():
    with open('cookies.json','r') as f:
        cookies = f.read()
        # print(cookies)
    nickname = os.getenv("NICKNAME")
    msg = os.getenv("MSG","火花")
    proxy = os.getenv("PROXY")
    proxy_file = os.getenv("PROXY_FILE", "china_proxies.txt")

    if not proxy:
        try:
            with open(proxy_file, 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                proxy = random.choice(proxies)
                print(f"从 {proxy_file} 中随机选择了一个代理: {proxy}")
        except FileNotFoundError:
            print(f"代理文件 {proxy_file} 未找到，将不使用代理。")
            proxy = None

    if proxy == '':
        proxy = None

    if cookies == '' or nickname == '':
        raise ValueError("SECRETS 未正确配置！")

    return {
        'cookies' : cookies,
        'nickname' : nickname,
        'msg' : msg,
        'proxy' : proxy
    }