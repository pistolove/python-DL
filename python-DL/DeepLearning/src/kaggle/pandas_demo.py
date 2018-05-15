#!/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

if __name__ == '__main__':
    s = pd.Series([100, 'python', 'soochow', 'qiwsir'])
    print s.values
    data = {"name": ["yahoo", "google", "facebook"], "marks": [200, 400, 800], "price": [9, 3, 7]}
    f1 = pd.DataFrame(data)
    print f1

    print "\n"
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print s

    print "\n"

    dates = pd.date_range('20130101', periods=6)
    print dates

    print "\n"

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print df
    print "\n"

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4,
                                      dtype='int32'),
                        'E': pd.Categorical(
                            ["test", "train", "test", "train"]),
                        'F': 'foo'})
    print df2
    print df2.dtypes
    print "\n"

    print df.head()
    print df.tail(2)
    print df.index
    print df.columns
    print df.values
    print df.describe()
    print df.T

    print df.sort_index(axis=1, ascending=False)

    print df.sort_values(by='B')

    print df['A']
    print df[0:3]

    print df.loc[dates[0]]

    print "\n"

# https://blog.csdn.net/zhu418766417/article/details/52718063