import numpy as np
import matplotlib.pyplot as plt
import cv2
import imageio

from src.preprocessors.filter import Filterer

img = imageio.imread(r"")

filterer = Filterer(filter_type="gaussian", img=img)
im_mean = filterer.apply_filter()