### [批量高清图片压缩](https://github.com/Rattenking/dev-python-tool/blob/master/python%203.7%20%E6%89%B9%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9/compressImg.py)
#### 环境
1. 安装 Pillow
```
  pip install Pillow
```
2. 运行环境
> python 3.7

#### 运行参数
```
filePath = os.path.dirname(os.path.abspath(__file__)) + '/'
fileNewPath = filePath + 'newimg/'
scale = 0.2
quality = 100
basename = 'newimg-'
```

|参数|说明|默认值|
|----|----|-----|
|filePath|当前工具运行的文件路径|'./'|
|fileNewPath|当前工具运行的文件夹下新建一个文件保存压缩后的图片|'./newimg/'|
|scale|图片宽高压缩比例，如原图100*200，压缩后20*40|0.2|
|quality|图片压缩后的模糊度|100|
|basename|图片压缩后重命名的前缀|newimg-|

#### 运行
```
  python compressImg.py
```

### [LOL 皮肤海报爬取](./python 3.7 LOL 皮肤海报爬取/downloadSkins.py)
#### 环境
1. 安装 requests
```
  pip install requests
```
2. 运行环境
> python 3.7

#### 运行参数
```
  skinsFolder = 'lol_skins'
```

|参数|说明|默认值|
|----|----|-----|
|skinsFolder|当前工具运行的文件路径保存皮肤海报的文件夹|'lol_skins'|

#### 运行
```
  python downloadSkins.py
```