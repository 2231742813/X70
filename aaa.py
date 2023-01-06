import json
import requests

URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=05e0f108-8ba3-45cb-ab50-fba37acf322c"  # Webhook地址


def post(url, data=None):
    data = json.dumps(data, ensure_ascii=False)
    data = data.encode(encoding="utf-8")
    r = requests.post(url=url, data=data)
    r = json.loads(r.text)
    return r


def markdown(markdown):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": markdown
        }
    }
    return post(URL, data)


if __name__ == "__main__":
    """Markdown类型"""
    print(markdown("# 一级标题\n ## 二级标题"))
    print(markdown("**Hello World!**"))
    print(markdown("[百度一下，你就知道](http://www.baidu.com/)"))
    print(markdown("`code`"))
    print(markdown("> 引用文字"))
    print(markdown('<font color="info">绿色</font>\n <font color="comment">灰色</font>\n <font color="warning">橙红色</font>'))
