﻿# Spam-Classifier

Breanna Powell and Melody Behdarvandian

CSS 576

Assignment 3

IDE: Visual Studio Code 

# Files enclosed:
spam-classifier.ipynb (run the program from this Jupyter Notebook)

emails.csv (our dataset from https://github.com/SmallLion/Python-Projects/blob/main/Spam-detection/spam.csv)

output.txt (the results of the hyperparameter search for the neural network)


# Setup
Follow these steps if you have not used Jupyter Notebooks in VS Code before:

https://code.visualstudio.com/docs/languages/python

Open Anaconda Navigator 

**Launch VS Code through Anaconda Navigator**

**Terminal > New Terminal**

https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/

1) Use the commands to create a tensorflow environment:

**$ conda create -n tf tensorflow**

**$ conda activate tf**

https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook

2) In the upper right hand corner, switch the kernel from "base" over to "tf(Python 3.10.9)"

This will change the kernel over to tensorflow's kernel.

3) Close this document and reopen it from Anaconda Navigator, but instead of "base" select "tf" from the dropdown menu

If you don't see "tf" in the dropdown menu, try closing Anaconda Navigator and reopening it.

4) Install the following:
**$ conda install ipykernel**

**$ conda install pandas matplotlib scikit-learn seaborn**

**$ conda install -c conda-forge tensorflow keras**

# Sections
The Spam-Classifier file is organized by the following

<details id=2>
<summary><h2>DATA EXPLORATION</h2></summary>
  
Check to see if there are missing values (NaN or null)

Check for Imbalanced Data

Remove any all duplicates in emails data

Check the ratio of ham to spam

</details>

<details id=3>
<summary><h2>PRE-PROCESSING TECHNIQUES</h2></summary>

Fix the Data Imbalance

Replace labels with 0 for ham and 1 for spam

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

</details>

<details id=3>
<summary><h2>MODEL BUILDING</h2></summary>
### Split into Train and Test
Split into training and testing data 80% training, 20% testing

### Neural Network
Get the shape of the data

Create a Sequential Keras model

Use Keras Callbacks Early Stopping

Optimize for precision

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
Use DBSCAN

Find the optimal value for epsilon and min_samples for 2 clusters

Look at the metrics
  
</details>
