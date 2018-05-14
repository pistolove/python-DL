#!/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

if __name__ == '__main__':
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    data = pd.read_csv('G://breast-cancer-wisconsin.data')
    # print data
    # data = data.replace(to_replace='? ', value=np.nan)
    data.describe()  # 数据描述，总结所有样本某一特征的均值，最大最小，平均值等。
    data = data.dropna(how='any')
    print data.shape
    # print data
