#!/bin/env python
# -*- coding: utf-8 -*-


with open("/Users/baidu/workspace/dmp-kg/automobile/automobile_etl2.py") as f:
    start_flag = False
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        if not start_flag and line == "\"\"\"":
            start_flag = True
        elif start_flag and line == "\"\"\"":
            break
        elif start_flag:
            arr = line.split(" ")
            if len(arr) != 3:
                print "#error " + line
                print
                continue
            name, name_type, comment = arr
            print "%s %s comment '%s'," % (name, name_type, comment)
