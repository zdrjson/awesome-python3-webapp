from PIL import Image, ImageFilter
##打开一个jpg的图像文件，注意是当前路径：
#im = Image.open('test.jpg')
#w, h = im.size
#print('Original image size: %sx%s' % (w, h))
## 缩放到50%
#im.thumbnail((w/2, h/2))
#print('Resize image to: %sx%s' % (w/2, h/2))
## 把缩放后的图像用jpeg格式保存：
#im.save('thumbnail.jpg','jpeg')


im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
	return chr(random.randint(65,90))
# 随机颜色1：
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
# 随机颜色2：
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
	






