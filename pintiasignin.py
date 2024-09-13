import requests
import re
import time
def get_cookies(email,password):
    login_url='https://passport.pintia.cn/api/users/sessions'
    login_data = {
        'email': email,
        'password': password,
        'rememberMe': False
    }
    headers = {
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Accept-Language': 'zh-CN',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json;charset=UTF-8',
        'Origin': 'https://pintia.cn',
        'Referer': 'https://pintia.cn/',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
    }
    session = requests.Session()
    response = session.post(login_url, headers=headers, json=login_data)

    if response.status_code == 200:

        cookies = session.cookies.get_dict()
        print("get cookies success:", cookies)
        response_data = response.json()
        nickname = response_data['user']['nickname']
        print(f"Nickname: {nickname}")
        return cookies,nickname


    else:
        print(f"Failed,Status：{response.status_code}, text：{response.text}")
        return None


def logout(cookies):
    delete_url = "https://pintia.cn/api/u/info"

    headers = {
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Accept-Language': 'zh-CN',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Eagleeye-Sessionid': 'RImew0zpz0pgy9i0ha6s1q54UUR4',
        'Accept': 'application/json;charset=UTF-8',
        'X-Marshmallow': '',
        'X-Lollipop': '7a54c4b59ec467c9b28cfb53c89a12a0',
        'Eagleeye-Pappname': 'eksabfi2cn@94d5b8dc408ab8d',
        'Eagleeye-Traceid': '17c9537a172615566222310108ab8d',
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

    response = requests.delete(delete_url, headers=headers, cookies=cookies, json=payload)

    if response.status_code == 200:
        print("logout")
    else:
        print(f"failed：{response.status_code}, response：{response.text}")

def sign_in(cookies):
    sign_in_url = "https://pintia.cn/api/users/checkin"
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
        print(f"Success, response: {response.text}")
    else:
        print(f"Failed,status code: {response.status_code}, response: {response.text}")

email = 'youremail'
password = 'passwd'
cookies,id = get_cookies(email, password)

print(id,end=' ')
sign_in(cookies)
print(id,end=' ')
logout(cookies)

