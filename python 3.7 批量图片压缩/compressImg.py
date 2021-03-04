"""
@Author  ：Rattenking
@Date    ：2021/02/09 10:27
@CSDN	 ：https://blog.csdn.net/m0_38082783
"""

from PIL import Image
import os
import time

filePath = os.path.dirname(os.path.abspath(__file__)) + '/'
fileNewPath = filePath + 'newimg/'
scale = 0.2
quality = 100
basename = 'newimg-'

# 获取当前文件夹下的文件名列表
def readname():
  names = None
  try:
    names = os.listdir(filePath)
  except Exception as e:
    print(e)
    print('获取文件名列表失败！')
  else:
    print('获取文件名列表成功！')
    return names

# 修改文件尺寸和压缩文件
def withDataImage(names):
  index = 1
  for name in names:
    suffix = name.split('.').pop()
    if suffix in ['jpg', 'png', 'jpeg', 'bmp']:
      img = Image.open(filePath + name)
      w,h = img.size
      w,h = round(w * scale),round(h * scale)
      img = img.resize((w,h), Image.ANTIALIAS)
      img.save('{}{}{}{}{}'.format(fileNewPath, basename, index, '.', suffix), optimize = True, quality = quality)
      index = index + 1

# 压缩时间的计算
def loopHandleFile():
  start = time.time()
  startTime = int(round(start * 1000))
  names = readname()
  try:
    if not os.path.exists(fileNewPath):
      os.makedirs(fileNewPath)
    withDataImage(names)
  except Exception as e:
    print(e)
    print('批量等比压缩图片失败！')
  else:
    print('批量等比压缩图片成功！')
    end = time.time()
    endTime = int(round(end * 1000))
    print('本次压缩用时：' + str(endTime - startTime) + ' ms')

if __name__ == "__main__":
  loopHandleFile()