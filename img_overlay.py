#expects greyscale images as inputs

from skimage.color import label2rgb, rgb2hsv, hsv2rgb
import numpy as np

def img_overlay(img,back,alpha):
	
	img_rgb = label2rgb(img)
	back_rgb = np.dstack((back,back,back))
	img_hsv = rgb2hsv(img_rgb)
	back_hsv = rgb2hsv(back_rgb)

	back_hsv[...,0] = img_hsv[...,0]
	back_hsv[...,1] = img_hsv[...,1]*alpha

	overlay = hsv2rgb(back_hsv)

	return overlay