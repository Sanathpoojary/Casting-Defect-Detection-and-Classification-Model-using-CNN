# -*- coding: utf-8 -*-
"""CastingDefectDetection&ClassificationModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfZW-WSaN6EvaytE1dVEa7E4yt2c37zJ
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

from tensorflow import keras
detection_model = keras.models.load_model('/content/drive/MyDrive/detection_model.h5')
classification_model = keras.models.load_model('/content/drive/MyDrive/classification_model.h5')

testimg='/content/drive/MyDrive/casting_data2/test/heat crack/cast_def_0_9880.jpeg'

import cv2
img = cv2.imread(testimg,0)
img = img/255
pred_img =img.copy()

plt.figure(figsize=(12,8))
plt.imshow(img,cmap='gray')
plt.show()

test_image = image.load_img(testimg,target_size=(64,64),color_mode='grayscale')
test_image = image.img_to_array(test_image)
test_image = test_image/255
test_image = np.expand_dims(test_image,axis=0)
result1 = detection_model.predict(test_image)

if result1[0]>=0.5:
    print('Not Defective')
else :
  result2 = classification_model.predict(test_image)
  print('The cast is found to be defective\nThe type of defect is:')
  if result2[0]<=0.5:
    print('Fins')
  else :
    print('Heat cracks')