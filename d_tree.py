# -*- encoding: utf-8 -*-
'''
@FILE           :d_tree.py
@TIME           :2020/05/10 11:40:25
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

决策树实现

version 1.0 暂时不包含连续性属性, 分类时只实现二分类
'''

import numpy as np
from split_functions import split_register

class TreeNode:
    def __init__(self, is_leaf=False, split_value=None, split_feature=None, split_idx=None, depth=None):
        """
        决策树中的节点类型的构造函数
        Args:
            is_leaf: 是否为叶子节点
            split_value: 分割值
        """
        self.is_leaf = is_leaf
        self.split_value = split_value
        self.split_feature = split_feature
        self.split_idx = split_idx
        self.depth = depth
        self.chiildren = None

    def get_decision_value(self):
        if self.is_leaf:
            return self.loss.get_decision_value()


# 计算基尼指数
def gini_index():
    pass

# 计算信息熵
def info_entropy():
    pass

# 计算信息增益
def info_gain():
    pass

class DecisionTree:
    
    def __init__(self, max_depth,features=None,optimizer='gini'):
        """
        Args:
            max_depth: int 决策树最大深度
            features: optional, List 属性名称，维度需要与之后的样本数据维度一致
            optimizer: 选择最优划分的依据，gini|infomation_entropy
        """
        self.max_depth = max_depth
        self.features = features
        self.optimizer = optimizer

    def __generate_tree__(self,x,y_true,fatures,depth_now=0):
        """
        x: list[list[float]] 输入数组,数组每个元素为一个样本数据，每个样本为维度为n的特征数组
        labels: 每个样本的类别
        fatures: 每个样本具有的特征名称列表
        """
        assert (
            len(x)>0,
            len(y_true)>0,
            len(features)>0
        ), "input data,lables or features should not be null or None"
        
        feature_num = len(fatures)
        viable_features = list(range(feature_num))
        
        # 继续划分的条件： 1.depth没达到max_depth 2.可用的特征数量大于0， 3.剩下的样本不止一类
        if depth_now<self.max_depth and \
            len(viable_features) > 0 and \
            len(np.unique(y_true)) > 1 :
            
            # 得到最优划分属性
            b_f_idx, b_f_name = split_register.get(self.optimizer)(x,y_true,features)
            
            #todo...
        