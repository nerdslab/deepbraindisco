# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:42:03 2019

@author: abalwani6
"""

#patch padding function
#x,y = pixel positions, p = size of patch, img_used = image to be used for patch extraction
#returns: paddedPatch = required patch, p = size of the patch

import numpy as np

def padPatch(x,y,p,img_used):
    
    m,n = img_used.shape

    if p%2==0:
        right = int(p/2)
        left = right
        up = int(p/2)
        down = up
    else:
        right = int(p/2)
        left = right+1
        up = int(p/2)
        down = up+1
        
    pad_left = 0
    pad_right = 0
    pad_up = 0
    pad_down = 0
    
    if x-left<0:
        pad_left = left-x
    if x+right>n:
        pad_right = (x+right)-n
    if y-up<0:
        pad_up = up-y
    if y+down>m:
        pad_down = (y+down)-m
    
    small_patch = img_used[(y-up+pad_up):(y+down-pad_down),(x-left+pad_left):(x+right-pad_right)]
    paddedPatch = np.pad(small_patch,((pad_up,pad_down),(pad_left,pad_right)),'constant',constant_values=((0,0),(0,0)))
    return paddedPatch, p

    def colourPatch(x,y,p,img_used,colour_px):
    
    m,n = img_used.shape

    if p%2==0:
        right = int(p/2)
        left = right
        up = int(p/2)
        down = up
    else:
        right = int(p/2)
        left = right+1
        up = int(p/2)
        down = up+1
        
    pad_left = 0
    pad_right = 0
    pad_up = 0
    pad_down = 0
    
    if x-left<0:
        pad_left = left-x
    if x+right>n:
        pad_right = (x+right)-n
    if y-up<0:
        pad_up = up-y
    if y+down>m:
        pad_down = (y+down)-m
    
    img_used[(y-up+pad_up):(y+down-pad_down),(x-left+pad_left):(x+right-pad_right)] = colour_px
    # paddedPatch = np.pad(small_patch,((pad_up,pad_down),(pad_left,pad_right)),'constant',constant_values=((0,0),(0,0)))
    return img_used