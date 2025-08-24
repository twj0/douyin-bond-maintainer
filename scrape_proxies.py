import requests
import json

def fetch_proxies_from_api():
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&country=cn&skip=0&proxy_format=protocolipport&format=json&limit=15"
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'origin': 'https://proxyscrape.com',
        'priority': 'u=1, i',
        'referer': 'https://proxyscrape.com/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if data and 'proxies' in data and data['proxies']:
            print("--- 成功获取的中国代理节点 ---")
            for proxy_info in data['proxies']:
                print(proxy_info['proxy'])
        else:
            print("API返回的数据为空或格式不正确。")

    except requests.exceptions.RequestException as e:
        print(f"请求API失败: {e}")
    except json.JSONDecodeError:
        print("解析JSON响应失败。")

if __name__ == "__main__":
    fetch_proxies_from_api()