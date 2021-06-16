#!/usr/bin/env python
"""
@Author  ：Rattenking
@Date    ：2021/06/10 16:05
@CSDN	 ：https://blog.csdn.net/m0_38082783
"""

import os
import time
import base64

# 将图片转换成base64
def img_to_base64(path):
  with open(path,"rb") as f:
    base64_data = base64.b64encode(f.read())
    return f'data:image/jpg;base64,{base64_data.decode()}'

# 获取文件列表中的图片列表
def get_all_images(files):
  images = []
  try:
    for name in files:
      suffix = name.split('.').pop()
      if suffix in ['jpg', 'png', 'jpeg', 'bmp']:
        images.append(name)
  except Exception as e:
    print(e)
  else:
    return images

# 获取文件夹下所有的文件
def get_all_file(path):
  names = None
  try:
    names = os.listdir(path)
  except Exception as e:
    print(e)
  else:
    return names

# 创建 js 文件，写入内容
def create_js_folder(path, foldername, base_imgs):
  try:
    with open(path + "/" + foldername + ".js", "w",encoding="utf-8") as js:
      js.writelines(base_imgs)
  except Exception as e:
    print(e)

# 获取 base64 的列表
def get_images_base64(path, files):
  jss = [
    "const icon = {\n"
  ]
  try:
    for name in files:
      suffix = name.split('.')[0]
      img_url = f'{path}/{name}'
      base_img = img_to_base64(img_url)
      jss.append(f'  "{suffix}Icon": "{base_img}",\n')
  except Exception as e:
    print(e)
  else:
    jss.append("}\n")
    jss.append("module.exports = icon;")
    return jss

if __name__ == "__main__":
  start_time = int(round(time.time() * 1000))
  path = "./"
  # 获取所有的文件
  files = get_all_file(path)
  
  # 获取所有的图片
  images = get_all_images(files)
  
  # 将图片列表转base64字符串
  icons = get_images_base64(path, images)

  # 创建 icon 的js文件
  create_js_folder(path, "icon", icons)

  end_time = int(round(time.time() * 1000))
  print(f'本次图片转换时间为：{end_time - start_time}ms')