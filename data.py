import cv2
import numpy as np 
import glob
import pickle

l = glob.glob('main/images/*.jpg')
print(len(l))
data = np.zeros([len(l),98,98,3])
i = 0
for image in l:
	data[i,:,:,:] = cv2.imread(image)
	print(i)
	i = i+1

pickle.dump(data,open('data.p','w'))
