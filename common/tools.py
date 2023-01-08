import datetime
import os


def get_now_time():
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目绝路径
    :return:
    """
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    # print(file_path[:file_path.find(project_name)+len(project_name)])
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    需获取文件路径拼接
    :param path:
    :param add_sep_before:
    :param add_sep_after:
    :return:
    """
    all_path = os.sep.join(path)
    # print(all_path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_image_path(image_name):
    """
    获取商品图片的路径
    :param image_name:
    :return:
    """
    img_dir_path = get_project_path() + sep(["img", image_name], add_sep_before=True)
    return img_dir_path


# if __name__ == '__main__':
#     # print(sep(["config", "environment.yaml"], add_sep_before=True))
#     print(get_image_path("商品图片book.jpg"))