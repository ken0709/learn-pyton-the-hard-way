# learn-pyton-the-hard-way
反斜杠的输入：option + ¥ = \
learn python
每章注释后面的不懂点
例如：ex8 为什么后面输出的时候一个逗号，一个双引号
#报错信息 ：
1) # 写中文注释的时候，运行报错，这是中英文编码的问题
解决的办法是：在第一行 填写 # -*- coding: utf-8 -*-

2) NameError: name 'false' is not defined
  解决办法 ：false 区分大小写的，改成False

3)NameError: name 'end9' is not defined
 解决办法： end9未定义，比如 end9 = 4

4)   File "ex8.py", line 5
SyntaxError: Non-ASCII character '\xe4'
解决办法： 在开头添加 -*- coding：utf-8 -*-
冒号要紧跟着coding，中间没有空格

5）Traceback (most recent call last):
  File "ex8.py", line 9, in <module>
    "I had this thing."
TypeError: not enough arguments for format string
原因：在第9行，包含信息里面，每个字符串换行后面都需要一个逗号，
解决办法：加上逗号

6） "I had this thing."，
                       ^
SyntaxError: invalid syntax

原因：在中文输入法下输入的时候
解决办法： 切换到英文输入 逗号

7)  python ex14.py no shanghai mac
Traceback (most recent call last):
  File "ex14.py", line 3, in <module>
    script, user_name = argv
ValueError: too many values to unpack

原因：后面的参数跟的太多了，应该只有1个？
解决办法：python ex14.py zed

8）
  File "ex14.py", line 6, in <module>
    print "Hi %s, I'm the %s script." % (user_name)
TypeError: not enough arguments for format string

原因：在第6行，没有填写足够的参数，漏掉了参数
解决：添加上print "Hi %s, I'm the %s script." % (user_name,script)

9) #ex16 ‘w’创建一个文件
10）ex17 copy文件内容 到一个新文件中
333
