# coding=utf-8
# @time: 2023/1/14 23:13
# Author: zjl

import aircv as ac
import cv2

from common.tools import get_project_path, sep, get_now_date_str
from common.report_add_img import add_img_path_2_report


class FindImg:
    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的图片路径
        :return:
        """
        img_source = self.img_imread(source_path)
        img_search = self.img_imread(search_path)
        result = ac.find_template(img_source, img_search)
        # cv2.rectangle函数的作用是在图像上绘制一个简单的矩形
        cv2.rectangle(img_source, result["rectangle"][0], result["rectangle"][3], (255, 0, 0), 2)
        diff_img_path = get_project_path() + sep(["img", "diff_img", get_now_date_str() + "-对比的图.png"],
                                                 add_sep_before=True)
        # cv2.imencode函数的作用是把处理过的图保存到指定路径
        cv2.imencode(".png", img_source)[1].tofile(diff_img_path)
        add_img_path_2_report(diff_img_path, "查找到的图")
        return result["confidence"]


if __name__ == '__main__':
    source_path = get_project_path() + sep(["img", "source_img", "img_source.jpg"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "assert_img", "head_img.jpg"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)
