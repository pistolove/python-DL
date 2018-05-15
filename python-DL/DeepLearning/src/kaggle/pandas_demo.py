#!/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


if __name__ == '__main__':
    s = pd.Series([100, 'python', 'soochow', 'qiwsir'])
    print s.values
    data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
    f1 = pd.DataFrame(data)
    print f1