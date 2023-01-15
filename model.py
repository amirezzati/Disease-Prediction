import pickle
import numpy as np
from keras.models import load_model

path = ".\Model\\"
model_loc = path + 'weights.hdf5'
classList_loc = path + 'output_classes.pkl'

# read output_classes using pickle
file_ = open(classList_loc, "rb")
output_classes = pickle.load(file_)
file_.close()


def predict(features):
    model = load_model(model_loc)
    result = model.predict(np.array([features]), verbose=0)
    class_num = np.argmax(result)

    return output_classes[class_num]
