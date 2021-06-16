#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 **********************************************************
 * Author        : tianshl
 * Email         : xiyuan91@126.com
 * Last modified : 2020-07-29 14:58:57
 * Filename      : img2gif.py
 * Description   : 图片转动图
 * Documents     : https://www.lcdf.org/gifsicle/
 * ********************************************************
"""
import argparse
import copy
import logging
import os
import random

from PIL import Image
from pygifsicle import optimize

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger(__name__)


class Img2Gif:
    """
    图片转动图
    """

    def __init__(self, img_path, blocks=16, mode='append', random_block=False):
        """
        初始化
        :param img_path:        图片地址
        :param blocks:          分块数
        :param mode:            展示模式 append: 追加, flow: 流式, random: 随机
        :param random_block:    随机拆分
        """
        self.mode = mode if mode in ['flow', 'append', 'random'] else 'append'

        self.blocks = blocks
        self.random_block = random_block

        # 背景图
        self.img_background = None

        self.img_path = img_path
        self.img_dir, self.img_name = os.path.split(img_path)
        self.img_name = os.path.splitext(self.img_name)[0]

        self.gif_path = os.path.join(self.img_dir, '{}.gif'.format(self.img_name))

    def get_ranges(self):
        """
        获取横向和纵向块数
        """
        if not self.random_block:
            w = int(self.blocks ** 0.5)
            return w, w

        ranges = list()
        for w in range(2, int(self.blocks ** 0.5) + 1):
            if self.blocks % w == 0:
                ranges.append((w, self.blocks // w))

        if ranges:
            return random.choice(ranges)
        else:
            return self.blocks, 1

    def materials(self):
        """
        素材
        """

        log.info('分割图片')
        img_origin = Image.open(self.img_path)
        (width, height) = img_origin.size
        self.img_background = Image.new(img_origin.mode, img_origin.size)

        # 单方向分割次数
        blocks_w, blocks_h = self.get_ranges()

        block_width = width // blocks_w
        block_height = height // blocks_h

        img_tmp = copy.copy(self.img_background)
        # 动图中的每一帧
        _materials = list()
        for h in range(blocks_h):
            for w in range(blocks_w):
                block_box = (w * block_width, h * block_height, (w + 1) * block_width, (h + 1) * block_height)
                block_img = img_origin.crop(block_box)
                if self.mode in ['flow', 'random']:
                    img_tmp = copy.copy(self.img_background)
                img_tmp.paste(block_img, (w * block_width, h * block_height))
                _materials.append(copy.copy(img_tmp))

        # 随机打乱顺序
        if self.mode == 'random':
            random.shuffle(_materials)

        log.info('分割完成')
        # 最后十帧展示原图
        [_materials.append(copy.copy(img_origin)) for _ in range(10)]
        return _materials

    def gif(self):
        """
        合成gif
        """

        materials = self.materials()
        log.info('合成GIF')
        self.img_background.save(self.gif_path, save_all=True, loop=True, append_images=materials, duration=250)
        log.info('合成完成')

        log.info('压缩GIF')
        optimize(self.gif_path)
        log.info('压缩完成')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--img_path", required=True, help="图片路径")
    parser.add_argument("-b", "--blocks", type=int, default=16, help="块数")
    parser.add_argument("-r", "--random_block", type=bool, default=False, help="随机拆分块数")
    parser.add_argument(
        '-m', '--mode', default='append', choices=['append', 'flow', 'random'],
        help="块展示模式 append: 追加, flow: 流式, random: 随机"
    )
    args = parser.parse_args()

    Img2Gif(**args.__dict__).gif()

