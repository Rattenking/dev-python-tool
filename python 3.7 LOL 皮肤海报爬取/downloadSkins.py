#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# https://lol.qq.com/data/info-heros.shtml
@Author  ：Rattenking
@Date    ：2021/02/22 16:19
@CSDN	 ：https://blog.csdn.net/m0_38082783
"""
import os
import json
import time
import requests

class DownloadLOLSkin():
  def __init__(self):
    self.heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    self.heroSkinsUrl = 'https://game.gtimg.cn/images/lol/act/img/js/hero/'
    self.skinsFolder = 'lol_skins'
    self.headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
      "Referer": "https://lol.qq.com/"
    }

  def getCurrentUrlData(self, url):
    """获取传入地址的数据"""
    results = None
    try:
      res = requests.get(url, headers = self.headers)
      results = json.loads(res.text)
    except Exception as e:
      print(e)
      return '获取【{}】数据失败！'.format(url)
    else:
      return results

  def getHeroList(self):
    """获取英雄列表"""
    heroList = self.getCurrentUrlData(self.heroListUrl)['hero']
    return heroList

  def getHeroSkinsList(self, heroId):
    """获取当前英雄皮肤列表"""
    heroSkinsList = self.getCurrentUrlData('{}{}{}'.format(self.heroSkinsUrl, heroId, '.js'))['skins']
    return heroSkinsList

  def downloadSkin(self, skinInfo):
    """根据传入皮肤信息，下载当前皮肤"""
    try:
      skinName = '{}{}'.format(skinInfo.get('name').replace('/','.'),'.jpg')
      skinId = skinInfo.get('skinId')
      mainImg = skinInfo.get('mainImg')
      # mainImg = 'https://game.gtimg.cn/images/lol/act/img/skin/big{}.jpg'.format(skinId)
      if mainImg != "":
        request = requests.get(mainImg)
        if request.status_code == 200:
          imgPath = os.path.join(self.skinsFolder, skinName)
          with open(imgPath, 'wb') as img:
            print('【{}】图片下载成功！'.format(skinInfo.get('name').replace('/','.')))
            img.write(request.content)
        else:
          print('【{}】图片下载失败！'.format(skinInfo.get('name').replace('/','.')))
    except Exception as e:
      print(e)
      print('{} 下载失败'.format(skinName))
      print('{} 下载失败图片地址'.format(mainImg))

  def downloadSkinsList(self, skinsList):
    """循环皮肤列表获取当前皮肤信息"""
    for skin in skinsList:
      self.downloadSkin(skin)
  
  def loopHeroListGetHeroId(self):
    """循环英雄列表获取当前英雄的heroId"""
    for hero in self.heroList:
      skinsList = self.getHeroSkinsList(hero.get('heroId'))
      self.downloadSkinsList(skinsList)
      
  def createFolder(self):
    """创建存放皮肤的文件夹"""
    if not os.path.exists(self.skinsFolder):
      os.mkdir(self.skinsFolder)

  def run(self):
    """运行当前脚本"""
    self.createFolder()
    self.heroList = self.getHeroList()
    startTime = int(round(time.time() * 1000))
    self.loopHeroListGetHeroId()
    endTime = int(round(time.time() * 1000))
    print('本次批量下载用时：{} ms'.format(endTime - startTime))
    
if __name__ == '__main__':
  lol = DownloadLOLSkin()
  # 执行脚本
  lol.run()
