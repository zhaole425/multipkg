#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: zhaole

import commands

def exe_cmd(cmd, output=True):
    status, content = commands.getstatusoutput(cmd)
    if output:
        print content
    if status:
        raise Exception("ERROR: %s" % content)

x,y = commands.getstatusoutput("ls")
print x
print y