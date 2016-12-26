# -*- coding: utf-8 -*-
my_name = 'Zed A. shaw' #我的名字叫
my_age = 35 #我的年龄
my_height = 74 #我的身高是
my_weight = 180 #我的体重是
my_eyes = 'blue' #我的眼睛是蓝色的
my_teeth = 'white' #我的牙齿是白色的
my_hair = 'brown' #我的头发是棕色的

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d i get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight)
