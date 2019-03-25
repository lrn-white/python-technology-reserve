import requests
import json

"""
爬虫案例1：
爬取豆瓣上的电影信息
"""


class DoubanSpilder:

    def __init__(self):
        self.temp_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend" \
                        "&page_limit=20&page_start={}"

    def get_content_list(self, html_str):
        """
        提取数据
        :param html_str: 从网页获取的数据
        :return:
        """

        dict_data = json.loads(html_str)
        content_list = dict_data["subjects"]
        return content_list

    def save_content_list(self, content_list):
        """
        存储数据
        :param content_list: 结构化的数据数组
        :return:
        """
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")

    # 实现主要逻辑
    def run(self):
        num = 0
        while num < 1000:
            start_url = self.temp_url.format(num)

            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/72.0.3626.121 Mobile Safari/537.36",
                "Refer": "https://movie.douban.com/explore"
            }

            response = requests.get(start_url, headers=headers)
            html_str = response.content.decode()

            content_list = self.get_content_list(html_str)

            self.save_content_list(content_list)

            num += 20


if __name__ == '__main__':
    case1 = DoubanSpilder()
    case1.run()
