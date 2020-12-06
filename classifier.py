### imports 
from PIL import Image
import numpy as np

labels = ["organic", "recyclable"]
# use an image of your choice and upload it then read it here
img = Image.open("O_10.jpg")


# convert img to a numpy array (see the eda.ipynb file use get_numpy_array function as example)
img_array = "" # you can do this

# load the model (simple_model) copy that exact code here 


model = "" # use same format as model_simple in other file

# compile model 

model.load_weights('models/simple_model.hdf5')

prediction = model.predict(img_array)

print(prediction) # this 