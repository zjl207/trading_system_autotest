# coding=utf-8
# @time: 2023/1/14 23:13
# Author: zjl

import aircv as ac

from common.tools import get_project_path, sep


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
        print(result)
        return result["confidence"]


# if __name__ == '__main__':
#     source_path = get_project_path() + sep(["img", "img_source.jpg"], add_sep_before=True)
#     search_path = get_project_path() + sep(["img", "head_img.jpg"], add_sep_before=True)
#     FindImg().get_confidence(source_path, search_path)
