# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter %("one","two","three","four") #为什么输出结果有单引号。
print formatter %(True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
     "I had this thing.",
     "That you could type up right.",
     "But it didn't sing.",
     "So i said goognight."
     )

#为什么打印出来的时候是一个单引号一个双引号
