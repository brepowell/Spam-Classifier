# Spam-Classifier

Melody Behdarvandian, Breanna Powell, and Angelo Williams

CSS 576

Final Project

IDE: Visual Studio Code 

# Contents

Content | Description
--------|------------
SpammedALot | folder with Django project and YouGotSpam app for user interface
data | folder with spam and ham data
emailsToFlag | folder where emails fetched from someone's gmail account will go
hyper-parameter-search-results | folder with txt files from results of hyperparameter search
saved-models | folder with saved machine learning models to use for deployment
visuals | folder with saved plots, like from Loading Vectors, and images, such as screenshots
allHamData.csv | data taken from raw format, then preprocessed, and saved as a CSV
allSpamData.csv | data taken from raw format, then preprocessed, and saved as a CSV
email-parser.ipynb | our parsing functions
email_features.csv  | features extracted from the real world data fetched from a user's gmail
email_fetching.py | fetches emails from a user's gmail account
email_parser.py | our parsing functions -- as a .py file
feature-analyzer.ipynb | 
hyperparam_search_testing.ipynb | 
loadMachineLearningModel.py | loads the best model that we have
project_File.ipynb | our new model building process for the final project
spam-classifier.ipynb | our original model building process


# Application
Our YouGotSpam app follows this pattern:

> Fetch all emails from an inbox and junk folder

> Save all as txt files

> Upload the emails to the database

> Preprocess the emails

> Feed the emails to the spam-classifier

> Flag emails as spam

> Notify user of all spam emails

To run the app, you must be in the same folder as manage.py

In the command line, type this:

> $ python manage.py runserver 8080

Open up a brower window.

Type this in the URL field:

> localhost:8080

# Code Setup & Libraries Needed
<details id=1>
<summary><h2>STEPS</h2></summary>
Follow these steps if you have not used Jupyter Notebooks in VS Code before:

https://code.visualstudio.com/docs/languages/python

Open Anaconda Navigator 

> Launch VS Code through Anaconda Navigator

> Terminal > New Terminal

https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/

1) Use the commands to create a tensorflow environment:

> $ conda create -n tf tensorflow

> $ conda activate tf

https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook

2) In the upper right hand corner, switch the kernel from "base" over to "tf(Python 3.10.9)"

This will change the kernel over to tensorflow's kernel.

3) Close this document and reopen it from Anaconda Navigator, but instead of "base" select "tf" from the dropdown menu

If you don't see "tf" in the dropdown menu, try closing Anaconda Navigator and reopening it.

4) Install the following for the project_File.ipynb:

> $ conda install ipykernel

> $ conda install pandas matplotlib scikit-learn seaborn

> $ conda install -c conda-forge tensorflow keras


</details>

# Machine Learning Model Process
The Spam-Classifier file is organized by the following sections:

<details id=2>
<summary><h2>DATA EXPLORATION</h2></summary>
  
Check for NaN or null values

Remove duplicates

Check for Imbalanced Data

Replace labels with 0 for ham and 1 for spam


</details>

<details id=3>
<summary><h2>PRE-PROCESSING TECHNIQUES</h2></summary>

Fix the Data Imbalance

Separate the features (x) from the labels (y)

### Feature Reduction
Apply a count vectorizer to the training data to convert from text to token counts

The count vectorizer will remove stop words from English (like "the" or "a") that have no bearing on spam or ham classification.

It cuts the features down to 40 key words.

### Normalizing the Data
Use MinMaxScaler from SKLearn to normalize the data

Mean Center data

Calculate the proportion of variance explained by each feature

Calculate the cumulative variance

Plot scree plot from PCA

### Feature importance with PCA
Show a bar graph of each word's importance

Print out which words from PCA[0] had the most importance

</details>

<details id=3>
<summary><h2>MODEL BUILDING</h2></summary>

### Split into Train and Test
Split into training and testing data 80% training, 20% testing

### Neural Network
Get the shape of the data

Create a Sequential Keras model

Use Keras Callbacks - Early Stopping

Set Epochs

Hyperparameter Search - Optimize for precision

Compile the model

Fit the model

### Metrics - compared with Testing Set
Evaluate the model against the testing set

### Saving the Model
Save the model as a json

Save the weights as h5 files

### Visual
Show a confusion matrix
</details>

<details id=3>
<summary><h2>CLUSTERING TECHNIQUES</h2></summary>
Hyperparameter Search - Optimize for Inertia

Use DBSCAN

Find the optimal value for epsilon and min_samples for 2 clusters

Look at the metrics
  
</details>
