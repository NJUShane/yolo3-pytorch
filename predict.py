#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
import os

from yolo import YOLO
from PIL import Image

yolo = YOLO()

testfile = open('%s.txt' % ('test'), 'w')
imgfile = 'img'
imglist = os.listdir(imgfile)
for img in imglist:
    try:
        image = Image.open(imgfile+'/'+img)
    except:
        str = img + ' can not open! Error!'
        print(str)
        continue
    else:
        # r_image = yolo.detect_image(image)
        # r_image.show()
        boxlist = yolo.generate_box(image)
        for box in boxlist:
            line = img + ',' + box + '\n'
            print(line)
            testfile.write(line)

testfile.close()