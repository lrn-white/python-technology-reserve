import requests

url = "https://translate.google.com/"

# 发送get请求
response = requests.get(url)
print(response)

# 发送post请求
data = {
    "view": "home",
    "op": "translate",
    "sl": "auto",
    "tl": "en",
    "text": "人生苦短，我用python"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": "https://translate.google.com/?source=gtx"
}
response2 = requests.post(url, data=data, headers=headers)
'''
response.text:显示返回内容,但该方法常常出现乱码,使用response.encoding = "utf-8"解决乱码
response.content.decode():把响应的二进制字节流转化为str类型
'''
response2.encoding = "utf-8"
print(response2.text)
