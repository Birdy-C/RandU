from PIL import Image
import sys

def  makeImageEven(image):#将图片色彩空间每个值的最后一位变成0
	pixels=list(image.getdata())#返回图像内容的像素值序列,[(r,g,b,t),(r,g,b,t)...]
	evenPixels=[(r&254,g&254,b&254,a&254) for [r,g,b,a] in pixels]
	evenImage=Image.new(image.mode,image.size)
	evenImage.putdata(evenPixels)
	return evenImage

def constLenBin(int):#内置函数bin()的替代，返回固定长度的二进制字符串
	binary = "0"*(8-(len(bin(int))-2))+bin(int).replace('0b','')
	return binary

def encodeDataInImage(image,data):#将字符串编码到图片中
	evenImage=makeImageEven(image)#获得最低有效位为0的图片副本
	binary = ''.join(map(constLenBin,bytearray(data, 'utf-8')))#将需要被隐藏的字符串转换成二进制字符串
	if len(binary) > len(image.getdata())*4: #如果不可能编码全部数据,抛出异常
		raise Exception("Error:The string is too long to be encoded into the image")
	encodedPixels = [(r+int(binary[index*4+0]),g+int(binary[index*4+1]),b+int(binary[index*4+2]),t+int(binary[index*4+3])) if index*4 < len(binary) else (r,g,b,t) for index,(r,g,b,t) in enumerate(list(evenImage.getdata()))] # 将 binary 中的二进制字符串信息编码进像素里
	encodedImage = Image.new(evenImage.mode, evenImage.size)#创建新图片以存放编码后的像素
	encodedImage.putdata(encodedPixels)#添加编码后的数据
	return encodedImage
'''
bytearray() 将字符串转换为整数值序列
bin() 的作用是将一个 int 值转换为二进制字符串
constLenBin()去掉bin()返回的二进制字符串中的'0b',并在左边补足'0'直到字符串长度为8
map(constLenBin,bytearray(data, ‘utf-8’))对数值序列中的每一个值应用constLenBin()函数,将十进制数值序列转换为二进制字符串序列
'''

img=sys.argv[1]
string=sys.argv[2]
encodeDataInImage(Image.open(img), string).save('D:/Imagewithword.png')
