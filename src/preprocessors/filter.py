import numpy as np
import cv2

class Filterer:
    def __init__(self, filter_type:str, img:np.array):
        self.filter = self._get_filter(filter_type)
        self.image = img
        
    def _get_filter(self, filter_type):
        if filter_type=="gaussian":
            return GaussianFilter()
        elif filter_type=="mean":
            return MeanFilter()

    def apply_filter(self):
        return self.filter(self.image)

class GaussianFilter:
    def __init__(self):
        pass
    
    def __call__(self, img:np.array, ksize:tuple=(5,5), sigmaX:int=0):
        return cv2.GaussianBlur(img, ksize, sigmaX)

class MeanFilter:
    def __init__(self):
        pass
    
    def __call__(self, img:np.array, ksize:tuple=(5,5)):
        return cv2.blur(img, ksize)
