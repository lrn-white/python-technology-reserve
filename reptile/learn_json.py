import json
import requests

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/72.0.3626.121 Mobile Safari/537.36",
    "Refer": "https://movie.douban.com/explore"
}

response = requests.get(url, headers=headers)
json_str = response.content.decode()

ret1 = json.loads(json_str)
print(ret1)

# ensure_ascii=False 不以AscII码的形式存储
# indent=2 使存入文本时下一行相比上一行空两格
with open("douban.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
