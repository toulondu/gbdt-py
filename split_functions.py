# -*- encoding: utf-8 -*-
'''
@FILE           :spilt_functions.py
@TIME           :2020/05/12 15:34:47
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

选择划分属性的函数： 信息熵 和 基尼指数
'''

from register import Registry

split_register = Registry('split_function')

@split_register.register('gini')
def get_best_feature_by_gini_index(self, x, y_true, features):
    """使用基尼指数获取最佳划分属性"""
    for i in features:
        cates = {}
        for sample in x:
            cates.get(x[i],[0,0])[y_true] += 1
            # todo...

@split_register.register('info_gain')
def get_best_feature_by_information_gain(self, x, y_true, features):
    """使用信息增益获取最佳划分属性"""
    pass # todo...