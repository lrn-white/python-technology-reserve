import requests
from fake_useragent import UserAgent

"""
splash演示
"""
url = "https://www.guazi.com/shaoxing/buy/"
# 加载文本
# splash_url = "http://172.17.111.87:32772/render.html?url={}&wait=1".format(url)
# 加载图片
lua_script = '''
function main(splash, args)
  splash:go('{}')
  splash:wait(1)
  return splash:html()
end
'''.format(url)
splash_url = "http://172.17.111.87:32772/execute?lua_source={}".format(lua_script)
response = requests.get(splash_url, headers={"User-Agent": UserAgent().random})
response.encoding = "utf-8"
print(response.text)
