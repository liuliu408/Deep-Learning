#!/usr/bin/python
# -*- coding: UTF-8 -*-
#!H:\Anaconda3\envs\new_labelme\python.exe
import argparse
import json
import os
import os.path as osp
import base64
import warnings
 
import PIL.Image
import yaml
 
from labelme import utils
 
import cv2
import numpy as np
from skimage import img_as_ubyte
 
# from sys import argv
 
def main():
    warnings.warn("This script is aimed to demonstrate how to convert the\n"
                  "JSON file to a single image dataset, and not to handle\n"
                  "multiple JSON files to generate a real-use dataset.")
 
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file')
    parser.add_argument('-o', '--out', default=None)
    args = parser.parse_args()
 
    json_file = args.json_file
 
    #freedom
    list_path = os.listdir(json_file)
    print('freedom =', json_file)
    for i in range(0,len(list_path)):
        path = os.path.join(json_file,list_path[i])
        if os.path.isfile(path):
 
            data = json.load(open(path))
            img = utils.img_b64_to_arr(data['imageData'])
            lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])
 
            captions = ['%d: %s' % (l, name) for l, name in enumerate(lbl_names)]
 
            lbl_viz = utils.draw_label(lbl, img, captions)
            out_dir = osp.basename(path).replace('.', '_')
            save_file_name = out_dir
            out_dir = osp.join(osp.dirname(path), out_dir)
 
            if not osp.exists(json_file + '\\' + 'labelme_json'):
                os.mkdir(json_file + '\\' + 'labelme_json')
            labelme_json = json_file + '\\' + 'labelme_json'
 
            out_dir1 = labelme_json + '\\' + save_file_name
            if not osp.exists(out_dir1):
                os.mkdir(out_dir1)
 
            PIL.Image.fromarray(img).save(out_dir1+'\\'+save_file_name+'_img.png')
            PIL.Image.fromarray(lbl).save(out_dir1+'\\'+save_file_name+'_label.png')
                
            PIL.Image.fromarray(lbl_viz).save(out_dir1+'\\'+save_file_name+
            '_label_viz.png')
 
            if not osp.exists(json_file + '\\' + 'mask_png'):
                os.mkdir(json_file + '\\' + 'mask_png')
            mask_save2png_path = json_file + '\\' + 'mask_png'
            ################################
            #mask_pic = cv2.imread(out_dir1+'\\'+save_file_name+'_label.png',)
            #print('pic1_deep:',mask_pic.dtype)
 
            mask_dst = img_as_ubyte(lbl)  #mask_pic
            print('pic2_deep:',mask_dst.dtype)
            cv2.imwrite(mask_save2png_path+'\\'+save_file_name+'_label.png',mask_dst)
            ##################################
 
            with open(osp.join(out_dir1, 'label_names.txt'), 'w') as f:
                for lbl_name in lbl_names:
                    f.write(lbl_name + '\n')
 
            warnings.warn('info.yaml is being replaced by label_names.txt')
            info = dict(label_names=lbl_names)
            with open(osp.join(out_dir1, 'info.yaml'), 'w') as f:
                yaml.safe_dump(info, f, default_flow_style=False)
 
            print('Saved to: %s' % out_dir1)
 
if __name__ == '__main__':
    #base64path = argv[1]
    main()
   
# 将本程序替换掉labelme/cli中的相应文件—json_to_dataset.py 。
# 在cmd中输入python json_to_dateset.py  /path/你的json文件夹的路径。
# 运行后，在json文件夹中会出现mask_png、labelme_json文件夹，mask_png中存放的是所有8位掩码文件！！！
#（不是16位，很多教程还得需要转换，我这里就不要转换了，一键生成，可右键png查看详细信息）。labelme_json文件夹中存放的是json解析后的图片。

