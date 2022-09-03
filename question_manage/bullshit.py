import random
import json

data = json.load(open("data.json", encoding="utf-8"))


def generator(title, length=800):
    """
    :param title: 文章标题
    :param length: 生成正文的长度
    :return: 返回正文内容
    """
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 40:
            body += "<p></p>"
        elif num < 60:
            body += random.choice(data["famous"]).\
                replace('a', random.choice(data["before"])).\
                replace('b', random.choice(data['after']))
        else:
            body += random.choice(data["bosh"])
        body = body.replace("x", title)

    return body


if __name__ == '__main__':
    content = generator("我爱Python")
    print(content)
    print(content)