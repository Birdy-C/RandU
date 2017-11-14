from PIL import Image
import sys

def binaryToString(binary):
	index = 0
	string = []
	rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
	fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
	while index + 1 < len(binary):
		chartype = binary[index:].index('0')
		length = chartype*8 if chartype else 8
		string.append(chr(int(fun(binary[index:index+length],chartype),2)))
		index += length
	return ''.join(string)

def decodeImage(image):#将字符串从图片中解码
	pixels=list(image.getdata())
	binary = ''.join([str(int((r&254)!=r))+str(int((g&254)!=g))+str(int((b&254)!=b))+str(int((a&254)!=a)) for (r,g,b,a) in pixels])#提取图片中所有最低有效位中的数据(跟原数据不一样就是加了1，一样就是加了0)
	locationDoubleNull = binary.find('0000000000000000')#找到数据截止处
	endIndex = locationDoubleNull+(8-(locationDoubleNull % 8)) if locationDoubleNull%8 != 0 else locationDoubleNull#找到数据截止位置的索引
	data = binaryToString(binary[0:endIndex])#提取所有的数据
	return data

imgwmark=sys.argv[1]
print(decodeImage(Image.open(imgwmark)))