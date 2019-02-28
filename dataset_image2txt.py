#制作txt文件
# -*- coding: utf-8 -*-
# @Author: liuqiang
# @Date:   2019-02-27 18:10:53

import os
train_file = open('VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
test_file = open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
for _, _, train_files in os.walk('data/train_dataset'):
    continue
for _, _, test_files in os.walk('data/test_dataset'):
    continue
for file in train_files:
    train_file.write(file.split('.')[0] + '\n')

for file in test_files:
    test_file.write(file.split('.')[0] + '\n')

---------------------------------------------------------------------------------------------------
#制作txt文件
# -*- coding: utf-8 -*-
# @Author: liuqiang
# @Date:   2019-02-27 18:10:53

import os
train_file = open('train.txt', 'w')   #指定train.txt文件路径
test_file  = open('test.txt', 'w')    #指定test.txt文件路径

for _, _, train_files in os.walk('train_dataset'):  #指定train_dataset训练图片路径
    continue
for _, _, test_files in os.walk('test_dataset'):    #指定test_dataset测试图片路径
    continue

for file in train_files:
    train_file.write(file.split('.')[0] + '\n')

for file in test_files:
    test_file.write(file.split('.')[0] + '\n')
