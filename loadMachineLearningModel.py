# HOW TO LOAD A MODEL:

from tensorflow.keras.models import model_from_json
import os

def loadMachineLearningModel():
    # Save to a folder as a txt file
    directory = "saved-models"
    workingDirectory = os.getcwd() #get current working directory
    path = os.path.join(workingDirectory, directory) 
    json_file = open(path+'\modelbinary_crossentropysgd1.00000.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(path+"\modelbinary_crossentropysgd1.00000.h5")
    print("Loaded model from disk")


loadMachineLearningModel()


