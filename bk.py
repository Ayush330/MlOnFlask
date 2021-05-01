import cv2 as cv
import numpy as np

img = cv.imread('cup.jfif',0)
print(img.shape)
x,y = img.shape[0],img.shape[1]
print(x,y)

'''new_img = np.zeros((x,y,1))

for i in range(x):
    for j in range(y):
        new_img[i][j]=img[i][j][0]
        #new_img.extend(img[i][j][0])

print(new_img.shape)
print(new_img)'''



for i in range(x):
    for j in range(y):
        if img[i][j] < 255/2:
            img[i][j]=0
        else:
            img[i][j]=255    


img = np.pad(img,((1,1),(1,1)),'minimum')

#cv.imshow('image',new_img)

x,y = img.shape[0],img.shape[1]
print(x,y)
print(img)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()