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

    proxies = []
    if not proxy:
        try:
            with open(proxy_file, 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                random.shuffle(proxies) # 打乱列表顺序
                print(f"从 {proxy_file} 加载了 {len(proxies)} 个代理。")
        except FileNotFoundError:
            print(f"代理文件 {proxy_file} 未找到，将不使用代理。")
    elif proxy:
        proxies.append(proxy)


    if cookies == '' or nickname == '':
        raise ValueError("SECRETS 未正确配置！")

    return {
        'cookies' : cookies,
        'nickname' : nickname,
        'msg' : msg,
        'proxies' : proxies # 返回整个列表
    }