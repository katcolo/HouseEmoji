import os, sys

import cv2

def log(msg):
    print('LOG >>> ' + msg)

if len(sys.argv) > 1:
    photo_folder = sys.argv[1]
else:
    log('No photo folder input; using default')
    photo_folder = './photos/'

print('photos from: ' + photo_folder)

try:
    # Try to lstat the folder to see if it exists
    os.lstat(photo_folder)
except:
    log('Photo folder [' + photo_folder + '] does not exist! Creating.')
    os.mkdir(photo_folder)

photo_list = os.listdir(photo_folder)
print('Photos in folder: ', len(photo_list))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

for photo in photo_list:
    print('  ', end='') #indent output.
    print(photo)

    img = cv2.imread(photo_folder + photo) #not os agnostic string
    cv2.imshow('image', img)
    key = cv2.waitKey(0)

cv2.destroyAllWindows()
