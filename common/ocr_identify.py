# coding=utf-8
# @time: 2023/1/23 19:32
# Author: zjl

import ddddocr


class OcrIdentify:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        """
        图片验证码识别
        :param pic_path:
        :return:
        """
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res
