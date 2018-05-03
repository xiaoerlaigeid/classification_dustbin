# -*- coding: utf-8 -*- 

from aip import AipImageClassify
import time

class_1 = '瓶' 
class_2 = '罐' 
class_3 = '盒' 


APP_ID = '11175215'
API_KEY = '0um3LZuIe4PXNaDGYAzjim9p'
SECRET_KEY = '98XKHseyvOq3hugthL7yGyHas0aL22sK'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY )

filePath = "21.jpg"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#def print_tmp( tmp ):
#	for i in tmp :
#		print i

def show_result( result ):
	tmp = [] 
	if isinstance(result, dict ):
		for data in result['result']:
			tmp.append( data['keyword'].encode('utf-8') )
	return tmp 

def check_plastic_bottle( tmp ):
	for i in tmp :
		if class_1 in i:
			return 1
	return 0
def check_can_bottle( tmp ):
	for i in tmp :
		if class_2 in i :
			return 1
	return 0
def chck_paper( tmp ):
	for i in tmp :
		if class_3 in i :
			return 1
	return 0

def recognize_picture( filePath ):
	result = client.advancedGeneral(get_file_content( filePath )
	tmp = show_result( result ) 
	if check_plastic_bottle( tmp ) == 1 :
		return 0
	if check_can_bottle( tmp ) == 1 :
		return 1
	if check_paper( tmp ) == 1 :
		return 2
	else
		return 3



# result = client.advancedGeneral(get_file_content( filePath ))

# for i in range(8):
# 	if i == 0:
# 		continue
# 	result = client.advancedGeneral(get_file_content( '2%d.jpg' % i ))
# 	show_result() 
# 	print '===\n'

# 	time.sleep(3)

