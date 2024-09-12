import requests
sign_in_url = "https://pintia.cn/api/users/checkin"


cookies = {
    '_bl_uid': 'yourcookie',
    '_ga': 'yourcookie',
    'JSESSIONID': 'yourcookie',
    'PTASession': 'yourcookie',
    '_ga_ZHCNP8KECW': 'yourcookie'
} 
headers = {
    'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
    'Accept-Language': 'zh-CN',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Eagleeye-Sessionid': 'O2m4g0e6zjg88XuqdmqUyX2jLzq7',
    'Accept': 'application/json;charset=UTF-8',
    'X-Marshmallow': '',
    'X-Lollipop': '7a54c4b59ec467c9b28cfb53c89a12a0',
    'Eagleeye-Pappname': 'eksabfi2cn@94d5b8dc408ab8d',
    'Eagleeye-Traceid': '7be3efe0172614279615510108ab8d',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://pintia.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://pintia.cn/market',
    'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=1, i'
}
payload = {}
response = requests.post(sign_in_url, headers=headers, cookies=cookies, json=payload)


if response.status_code == 200:
    print("Success")  
else:
    print(f"Failed,status code: {response.status_code}, response: {response.text}")



