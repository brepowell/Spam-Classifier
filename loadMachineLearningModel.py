# HOW TO LOAD A MODEL:

from tensorflow.keras.models import model_from_json
import os
import pandas as pd


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
    return loaded_model


from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

def preprocessEmails():
    stList = text.ENGLISH_STOP_WORDS
    stList = list(stList)
    emailToClassify = pd.read_csv('email_features.csv')
    ourStopWords = ['www', 'com', 'php', 'https', 'xml','org','uk', 'net', 'like', 'html', 'http', 'index',
            'hml', 'htm', 'just', 'know', 'yahoo', 've', 'way', 'linux', 'said', 'day', 'time', 'ca', 'url', 
            'did', 'bruce']
    stopWords = ourStopWords + stList
    cv = CountVectorizer(strip_accents= "unicode", stop_words=stopWords, max_features=30) # This cuts the features to 40 words
    features = cv.fit_transform(emailToClassify)
    columns = cv.get_feature_names_out()
    emailToClassify = pd.DataFrame(features.toarray()) # convert it to an dataframe instead
    emailToClassify.columns = columns
    print(columns)
    from sklearn.preprocessing import MinMaxScaler
    import numpy as np
    scaler = MinMaxScaler() # transform data
    emailToClassify = scaler.fit_transform(emailToClassify)
    emailToClassify = emailToClassify-np.mean(emailToClassify,axis=0)

    return emailToClassify

