import io
from script import base
import requests
import re
import os
from web import models
import datetime

name_1 = './photo/'


def getImgList(userid, target, pn):
    num = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/84.0.4147.125 Safari/537.36'}
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + target + '&pn=' + pn + '&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0 '
    res = requests.get(url, headers=headers)
    htlm_1 = res.content.decode()
    #print(htlm_1)
    a = re.findall('"objURL":"(.*?)",', htlm_1)
    if re.findall(r'找到相关图片约.*张', htlm_1):
        findnum = re.findall(r'找到相关图片约.*张', htlm_1)[0].replace(',', '')
        num = findnum.split('约', 1)[1]
        num = num.split("张")[0]
    else:
        findnum = re.findall(r'找到相关图片.*张', htlm_1)[0].replace(',', '')
        num = findnum.split('片', 1)[1]
        num = num.split("张")[0]
    return num, findnum, a
    # if not os.path.exists(name_1):
    #     os.makedirs(name_1)
    # for b in a:
    #     print(x, num)
    #
    #     if num == int(x):
    #         break
    #     else:
    #         try:
    #             img = requests.get(b)
    #             image_b = io.BytesIO(img.content).read()
    #             size = len(image_b)
    #             if size < 1e4:  # 小于10kb
    #                 continue
    #             print("{} kb\n".format(size / 1e3))
    #
    #         except Exception as e:
    #             print('第' + str(num) + '张图片无法下载------------')
    #             print(str(e))
    #             continue
    #
    #         print('---------正在下载第' + str(num + 1) + '张图片----------')
    #         f = open(name_1 + name + str(num + 1) + '.jpg', 'ab')
    #         f.write(img.content)
    #         f.close()
    #         num = num + 1
    # models.UserHistory.objects.create(
    #     username=username,
    #     mobile_phone=tel,
    #     search=name,
    #     date=datetime.datetime.now()
    # )


if __name__ == '__main__':
    print(getImgList(userid=3, target="张恪靖", pn="0")[0])
    print(getImgList(userid=3, target="张恪靖", pn="0")[1])
