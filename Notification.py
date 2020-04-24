#! usr/bin/env python3
#-*- coding: utf-8 -*-

import random

# 定义同义词
according = ["根据","按照"]
department = ["上级","教育部","有关单位","上级部门","有关部门"]
ands = ["和","以及","、"]
about = ["关于","有关"]
semester = ["春学期","本学期","春季学期"]
jobs = ["开学工作","返校工作"]
require = ["要求","相关规定","相关要求"]
# 这个字太灵性了所以特地用中文
起 = "起"
arrange = ["启动","安排"]
principle = ["分期","分批","错时","有序","错峰"]
college = ["学院","学院(系)","培养单位"]
every = ["各位","每位",""]
student = ["学生","同学"]
para = ["\n  ",""]
strict = ["严格","务必",""]
ends = ["。","，"]

# 输入学校和日期
university = input("请输入发布通知的大学:")
time = input("请输入发布通知的时间:")

# 随机选择词汇
def r(words):
    return random.sample(words,1)[0]


# 打印标题
title = university + r(about) + "2020年" + r(semester) + r(jobs) + "的通知"
print("\n\n\t" + title)

# 打印内容
sentence_1 = "  " + r(according) + r(ands).join(random.sample(department,2)) + r(about) + "2020年" +  r(semester) + r(jobs) + "的" + r(require) + "，"

sentence_2 = "结合学校疫情防控工作实际，经研究，定于2020年" + time + 起 + r(arrange) + "学生" + "".join(random.sample(principle,3)) + "返校" + r(ends)

sentence_3 = "具体返校时间" + random.sample(ands,1)[0] + random.sample(require,1)[0] + "由各" + r(college) + "通知" + r(every) + r(student)

sentence_3 = r(para) + "请" + r(every) + r(student) + r(strict) + r(according) + "通知" + r(require) + "返校并做好自我防护。" 

print(sentence_1 + sentence_2 + sentence_3)

print("\n\n\t\t\t\t\t"+ university + "\n" + " \t\t\t\t\t2020年" + time + "\n\n")