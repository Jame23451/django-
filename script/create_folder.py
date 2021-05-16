import os

import requests


def addUser(user_id):
    path = "/Users/jamesccc/Downloads/django--master-2/media/" + user_id
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")


def addAlbum(user_id, filename):
    path = "/Users/jamesccc/Downloads/django--master-2/media/" + user_id + '/' + filename
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")


def addImgToAlbum(user_id, project, filename, url):
    path = "/Users/jamesccc/Downloads/django--master-2/web/static/media/" + str(user_id) + '/' + project
    print(path)
    img = requests.get(url)
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    path += '/' + str(filename)
    f = open(path + '.jpg', 'ab')
    print(f)
    f.write(img.content)


url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fstefankanchev.com%2Fimg%2Flogos%2F84-1.gif&refer=http%3A%2F%2Fstefankanchev.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622913206&t=ad7615abe884b4397572919b5ff217ce"
addImgToAlbum(str(3), "我是毕设", "D", url)
