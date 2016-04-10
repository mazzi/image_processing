import cv2
import numpy as np

BASE_PATH ='./images/'
IMG_01 =  'allmighty.jpg'

#   cv2.COLOR_RGB2GRAY
#   cv2.COLOR_BGR2RGB
def readimage(img_path, cv2_color=False):
    img = cv2.imread(img_path)
    if cv2_color:
        img = cv2.cvtColor(img, cv2_color)
    return img

def saveimage(img, name, prefix=False):
	if prefix:
		cv2.imwrite(BASE_PATH + prefix + name, img)
	else:
		raise ValueError('A prefix should be specified!')

def transform_grayscale_and_save(img, name, prefix):
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    saveimage(gray_img, name, 'gray_', )
    return gray_img

def average_color(img):
    average_color_per_row = np.average(img, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    average_color = np.uint8(average_color)
    return average_color

def threshold_and_save(gray_img, name, prefix):
    _, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)
    threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)
    saveimage(threshold_img, name, prefix)

if __name__ == "__main__":
    img = readimage(BASE_PATH + IMG_01)
    gray_img = transform_grayscale_and_save(img, IMG_01, 'gray_')
    threshold_and_save(gray_img, IMG_01, 'threshold_')

