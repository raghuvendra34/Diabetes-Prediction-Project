# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('/Users/raghuvendrakumar34gmail.com/Downloads/Deploying Machine Learning Model/trained_model.sav', 'rb'))


input_data = (6,148,72,35,0,33.6,0.627,50)

# changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is Non Diabetic')
else:
  print('The person is Diabetic')
  
  
  
