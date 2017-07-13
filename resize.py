import cv2
import glob

names = glob.glob('images/images_2/*.jpg')
i=1564
for name in names:
	img = cv2.imread(name)
	img = cv2.resize(img,(98,98))
	print(img.shape)
	new_name = 'main/images/%s.jpg'%i
	print(new_name)
	i = i+1	
	cv2.imwrite(new_name,img)
	# print(name)
