# -*- coding: utf-8 -*-
import Augmentor
from Augmentor import Operations
import sys
# p = Augmentor.Pipeline("//data/pzndata/augmentor/swfori/A/full-VOC(baby)20190629/JPEGImages/")
p = Augmentor.Pipeline(sys.argv[1])
# p = Augmentor.Pipeline(sys.argv[1])
# Point to a directory containing ground truth data.
# Images with the same file names will be added as ground truth data
# and augmented in parallel to the original data.
# p.ground_truth("/data/pzndata/augmentor/swfori/A/full-VOC(baby)20190629/SegmentationClass/")
p.ground_truth(sys.argv[2])
# Add operations to the pipeline as normal:
# p.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=5)
# # p.random_brightness(probability=1,min_factor=0.5, max_factor =1.5)
p.random_brightness(probability=1,min_factor=0.5, max_factor =1)
p.random_color(probability=1,min_factor=1, max_factor =1.5)
# p.random_color(probability=1,min_factor=1, max_factor =1.5)
p.skew_tilt(0.2,0.5)
p.scale(0.3,1.5)
# p.random_erasing(1,0.9)
# # p.mixup(probability=1,min_factor=1, max_factor =1.5)
p.flip_left_right(probability=0.5)
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.crop_random(probability=0.4, percentage_area=0.5)
p.zoom_random(probability=0.3, percentage_area=0.8)
p.flip_top_bottom(probability=0.5)
p.sample(500)
