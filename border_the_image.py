import numpy as np
import pandas as pd
import cv2

img=cv2.imread('../resized_nearest.jpg')
mewd = np.pad(img, ((20,20), (20, 20), (0,0)))

data = pd.DataFrame(mewd.reshape(460*355, 3))

data.to_csv('output.csv', index=False)