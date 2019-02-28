# -*- coding:utf-8 -*-
# !/usr/bin/env python

import argparse
import json
import matplotlib.pyplot as plt
import skimage.io as io
import cv2
from labelme import utils
import numpy as np
import glob
import PIL.Image
from shapely.geometry import Polygon#https://shapely.readthedocs.io/en/latest/manual.html#geometric-objects

class labelme2coco(object):
    def __init__(self,labelme_json=[],save_json_path='D:/haidee/new/'):
        '''
        :param labelme_json: 所有labelme的json文件路径组成的列表
        :param save_json_path: json保存位置
        '''
        self.labelme_json=labelme_json#所有的json文件
        self.save_json_path=save_json_path#输出文件new.json的路径
        self.images=[]
        self.categories=[]
        self.annotations=[]
        # self.data_coco = {}
        self.label=[]
        self.annID=1
        self.height=0
        self.width=0

        self.save_json()

    def data_transfer(self):#在这里修改label的截断以符合自己的数据
        for num,json_file in enumerate(self.labelme_json):#给每个json文件标上序号num，json_file是序号对应的文件名
            with open(json_file,'r') as fp:#只读打开一个json为fp
                data = json.load(fp)  # 加载刚刚的fpjson文件到data
                self.images.append(self.image(data,num))#append添加到list的末尾，调用iamge类
                #print(data['shapes'])#json文件中shapes里的全部内容
                #[{'label': 'c_c_1', 'line_color': None, 'fill_color': None, 'points': [[306.0, 29], [307, 153],
                #[321, 163], [342, 165], [354, 151], [349, 27], [334, 15], [319, 15]]}, {'label': 'c_c_2', 'line_color':
                #None, 'fill_color': None, 'points': [[251.0, 164], [359, 165], [371, 170], [379, 187], [374, 202],
                #[362, 213], [250, 215], [235, 207], [231, 188], [238, 170]]}, {'label': 'c_c_3', 'line_color': None,
                #'fill_color': None, 'points': [[203.0, 234], [307, 214], [325, 214], [339, 227], [342, 246], [330, 261],
                #[221, 281], [206, 274], [193, 252]]}, {'label': 'c_c_4', 'line_color': None, 'fill_color': None, 'points':
                #[[228.0, 183], [307, 86], [307, 73], [287, 58], [269, 61], [191, 150], [194, 171], [207, 183]]}, {'label':
                #'c_c_5', 'line_color': None, 'fill_color': None, 'points': [[134.0, 123], [193, 227], [193, 248], [178, 262],
                #[159, 256], [98, 151], [99, 132], [117, 118]]}, {'label': 'c_c_6', 'line_color': None, 'fill_color': None,
                #'points': [[128.0, 242], [234, 287], [241, 306], [234, 323], [214, 329], [113, 289], [101, 269], [111, 252]]},
                #{'label': 'c_c_7', 'line_color': None, 'fill_color': None, 'points': [[355.0, 231], [274, 312], [273, 330],
                #[287, 345], [301, 348], [389, 261], [388, 239], [371, 229]]}]
                for shapes in data['shapes']:
                    #label=shapes['label'].split('_')
                    label=shapes['label']#[:-1]#提取shapes里的label
                    #print(shapes['label'])
                    #print(label)
                    if label not in self.label:
                        self.categories.append(self.categorie(label))
                        self.label.append(label)
                    points=shapes['points']
                    points[0][0]=1.0*points[0][0]
                    #print(points)
                    self.annotations.append(self.annotation(points,label,num))
                    self.annID+=1
        #print(self.label)

    def image(self,data,num):
        image={}
        img = utils.img_b64_to_arr(data['imageData'])  # 解析原图片数据
        # img=io.imread(data['imagePath']) # 通过图片路径打开图片
        # img = cv2.imread(data['imagePath'], 0)
        height, width = img.shape[:2]
        img = None
        image['height']=height
        image['width'] = width
        image['id']=num+1
        image['file_name'] = data['imagePath'].split('/')[-1]

        self.height=height
        self.width=width

        return image

    def categorie(self,label):
        categorie={}
        categorie['supercategory'] = label
        categorie['id']=len(self.label)+1 # 0 默认为背景
        categorie['name'] = label
        return categorie

    def annotation(self,points,label,num):
        annotation={}
        annotation['segmentation']=[list(np.asarray(points).flatten())]
        poly = Polygon(points)
        area_ = round(poly.area,6)
        annotation['area'] = area_
        annotation['iscrowd'] = 0
        annotation['image_id'] = num+1
        # annotation['bbox'] = str(self.getbbox(points)) # 使用list保存json文件时报错（不知道为什么）
        # list(map(int,a[1:-1].split(','))) a=annotation['bbox'] 使用该方式转成list
        annotation['bbox'] = list(map(float,self.getbbox(points)))

        annotation['category_id'] = self.getcatid(label)
        annotation['id'] = self.annID
        return annotation

    def getcatid(self,label):
        for categorie in self.categories:
            if label==categorie['name']:
                return categorie['id']
        return -1

    def getbbox(self,points):
        # img = np.zeros([self.height,self.width],np.uint8)
        # cv2.polylines(img, [np.asarray(points)], True, 1, lineType=cv2.LINE_AA)  # 画边界线
        # cv2.fillPoly(img, [np.asarray(points)], 1)  # 画多边形 内部像素值为1
        polygons = points
        mask = self.polygons_to_mask([self.height,self.width], polygons)
        return self.mask2box(mask)

    def mask2box(self, mask):
        '''从mask反算出其边框
        mask：[h,w]  0、1组成的图片
        1对应对象，只需计算1对应的行列号（左上角行列号，右下角行列号，就可以算出其边框）
        '''
        # np.where(mask==1)
        index = np.argwhere(mask == 1)
        rows = index[:, 0]
        clos = index[:, 1]
        # 解析左上角行列号
        left_top_r = np.min(rows)  # y
        left_top_c = np.min(clos)  # x

        # 解析右下角行列号
        right_bottom_r = np.max(rows)
        right_bottom_c = np.max(clos)

        # return [(left_top_r,left_top_c),(right_bottom_r,right_bottom_c)]
        # return [(left_top_c, left_top_r), (right_bottom_c, right_bottom_r)]
        # return [left_top_c, left_top_r, right_bottom_c, right_bottom_r]  # [x1,y1,x2,y2]
        return [left_top_c, left_top_r, right_bottom_c-left_top_c, right_bottom_r-left_top_r]  # [x1,y1,w,h] 对应COCO的bbox格式

    def polygons_to_mask(self,img_shape, polygons):
        mask = np.zeros(img_shape, dtype=np.uint8)
        mask = PIL.Image.fromarray(mask)
        xy = list(map(tuple, polygons))
        PIL.ImageDraw.Draw(mask).polygon(xy=xy, outline=1, fill=1)
        mask = np.array(mask, dtype=bool)
        return mask

    def data2coco(self):
        data_coco={}
        data_coco['images']=self.images
        data_coco['categories']=self.categories
        data_coco['annotations']=self.annotations
        return data_coco

    def save_json(self):
        self.data_transfer()
        self.data_coco = self.data2coco()
        # 保存json文件
        json.dump(self.data_coco, open(self.save_json_path, 'w'), indent=4)  # indent=4 更加美观显示

labelme_json=glob.glob('./*.json')#获取当前目录下的所有.json文件
# labelme_json=['./1.json']

lab = labelme2coco(labelme_json,'D:/haidee/new/new.json')#调用labelme2coco类
print('Saved to :',lab.save_json_path)
