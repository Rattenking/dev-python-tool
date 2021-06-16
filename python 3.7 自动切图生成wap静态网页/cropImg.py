#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
@Author  ：Rattenking
@Date    ：2021/04/07 09:55
@CSDN	 ：https://blog.csdn.net/m0_38082783
"""

# 导入相关的库
from PIL import Image
import win32ui
import os

class CreateHTML():
  def __init__(self):
    # 获取图片切割数量
    self.imgnum = input("请输入图片切割张数：")
    while True:
      try:
        self.imgnum = int(self.imgnum)
        break
      except:
        self.imgnum = input("输入错误，只能为数字，请输入图片切割张数：")

    self.htmlname = input("请输入 HTML 名称：")
    # 选择切割图片
    self.filename = self.chooseImg()
    # 获取切割图片的文件夹路径并创建images文件夹
    self.folder = os.path.dirname(self.filename)
    self.createFolder(self.folder + "/images")
    # 切割图片的初始化参数
    self.initParams()
    # 切割图片
    self.cropImg(self.y, self.index)

  def initParams(self):
    self.img = Image.open(self.filename)
    # 图片尺寸
    img_size = self.img.size
    self.h = img_size[1]  # 图片高度
    self.w = img_size[0]  # 图片宽度
    self.x = 0
    self.y = 0
    self.index = 1
    self.imgh = self.h / self.imgnum

  def chooseImg(self):
    """打开文件对话框选择图片"""
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir("C:/")  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    filename = dlg.GetPathName()  # 获取选择的文件名称
    return filename

  def cropImg(self, y, index):
    # 开始截取
    region = self.img.crop((self.x, y, self.w, y + self.imgh))
    # 保存图片
    region.save( self.folder + "/images/" + str(index) + ".png")
    if index < self.imgnum:
      self.cropImg(y + self.imgh, index + 1)
    else:
      self.createHtmlFolder()

  def createHtmlFolder(self):
    html = open(self.folder + "/" + self.htmlname + ".html", "w",encoding="utf-8")
    html.writelines(self.createHtmlStr())
    html.close()

  def createFolder(self, folder):
    """创建存放切图后图片存放文件夹"""
    if not os.path.exists(folder):
      os.mkdir(folder)

  def createHtmlStr(self):
    htmls = [
      "<!DOCTYPE html>\n",
      "<html lang=\"en\">\n",
      "<head>\n",
      "  <meta charset=\"utf-8\">\n",
      "  <meta content=\"email=no\" name=\"format-detection\">\n",
      "  <meta content=\"telephone=no\" name=\"format-detection\">\n",
      "  <meta name=\"msapplication-tap-highlight\" content=\"no\">\n",
      "  <meta content=\"yes\" name=\"apple-mobile-web-app-capable\">\n",
      "  <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n",
      "  <meta content=\"black\" name=\"apple-mobile-web-app-status-bar-style\">\n",
      "  <meta content=\"width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no\" name=\"viewport\">\n",
      "  <link rel=\"shortcut icon\" href=\"https://www.tyfo.com/market/content/home_image/favicon.ico\" type=\"image/x-icon\" />\n",
      "  <title>{}</title>\n".format(self.htmlname),
      "  <link rel=\"stylesheet\" href=\"https://www.tyfo.com/common/js/tui.css\">\n",
      "  <script src=\"https://www.tyfo.com/common/js/tui.js\"></script>\n",
      "  <script src=\"https://www.tyfo.com/common/js/jquery.js\"></script>\n",
      "  <script src=\"https://m.tyfo.com/wap/js/myjs/vue.js\"></script>\n",
      "  <script src=\"https://m.tyfo.com/wap/js/myjs/vant.js\"></script>\n",
      "  <link rel=\"stylesheet\" href=\"https://m.tyfo.com/wap/js/myjs/vant.css\">\n",
      "  <style>\n",
      "      .tui-content{\n",
      "        width: 100%;\n",
      "        min-width: 320px;\n",
      "        max-width: 750px;\n",
      "      }\n",
      "      .rui-pr{position:relative;}\n",
      "  </style>\n",
      "</head>\n",
      "<body>\n",
      "  <div class=\"tui-content\" id=\"app\">\n"
    ]
    # 循环添加图片字符串
    for index in range(self.imgnum):
      htmls.append("     <img src=\"./images/{}.png\" class=\"tui-full\"/>\n".format(index + 1))
    htmls.append("  </div>\n")
    htmls.append("  <script>\n")
    htmls.append("    var app = new Vue({el: \"#app\"})\n")
    htmls.append("  </script>\n")
    htmls.append("</body>\n")
    htmls.append("</html>\n")
    return htmls

if __name__ == "__main__":
  CreateHTML()