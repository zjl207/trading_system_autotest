# coding=utf-8
# @time: 2023/1/8 22:40
# Author: zjl

class GoodsBase:
    def goods_title(self):
        """
        商品标题
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        商品详情
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        商品数量
        :param plus: 如果为True,则使用加号，为False,则直接输入数量
        :return:
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']//parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_image(self):
        """
        商品图片
        :return:
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        商品单价
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        选择商品状态
        :param select_name:上架、下架
        :return:
        """
        return "//span[text()='" + select_name + "']//parent::li"

    def goods_bottom_button(self, button_name):
        """
        新增二手商品底部按钮
        :param button_name: 提交、重置
        :return:
        """
        return "//span[text()='" + button_name + "']//parent::button"
