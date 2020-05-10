# -*- encoding: utf-8 -*-
'''
@FILE           :d_tree.py
@TIME           :2020/05/10 11:40:25
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

决策树实现

version 1.0 暂时不包含连续性属性
'''

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

    def __generate_tree__(self,X,labels):
        pass

