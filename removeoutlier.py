# -*- coding: utf-8 -*-


import os
import cv2

oripath = "/data/pzndata/augmentor/newendoscope/data25/JPEGImages/output/"
dstpath = "/data/pzndata/augmentor/newendoscope/data25/output25gt/gtcolor/"

# width = 1024
# height = 768
# for filename in os.listdir(path):
    # im = cv2.imread(path + filename)
    # # if im.shape[1]==2592:
        # # tempimg = cv2.resize(im, (width, height), cv2.INTER_LINEAR)
    # tempimg = im*100
    # cv2.imwrite(path1 + filename, tempimg)
for filename in os.listdir(oripath):
    if 'ground' in filename:
        im = cv2.imread(oripath + filename)
        # if im.shape[1]==2592:
            # tempimg = cv2.resize(im, (width, height), cv2.INTER_LINEAR)
        im[im>3]=0
        # tempimg = im*100
        cv2.imwrite(dstpath + filename,im)
