from retrying import retry
import requests


@retry(stop_max_attempt_number=3)
def _parse_url(url):
    """
    请求失败时会自动重复三次
    """
    print("*" * 10)
    response = requests.get(url, timeout=5)
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"
    url1 = "www.baidu.com"
    # print(parse_url(url))
    print(parse_url(url1))
