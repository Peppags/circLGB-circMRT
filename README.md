# circLGB & circMRT 
## Overview
Identifying circular RNA and predicting its regulatory interactions by machine learning.

## Pre-requisite:  
* **Ubuntu 16.04**
* **Anaconda 3-5.2.0**
* **Python packages:**   
  [numpy](https://numpy.org/) 1.16.4  
  [pandas](https://pandas.pydata.org/) 0.23.0  
  [scikit-learn](https://scikit-learn.org/stable/) 0.19.1  
  [scipy](https://www.scipy.org/) 1.1.0   
  [lightgbm](https://github.com/Microsoft/LightGBM) 
  
## Installation guide
#### **Operation system**  
Ubuntu 16.04 download from https://www.ubuntu.com/download/desktop  
#### **Python and packages**  
Download Anaconda 3-5.2.0 tarball on https://www.anaconda.com/distribution/#download-section  
#### **lightgbm installation:**  
pip install lightgbm  
  
## Content  
#### **data**   
* **circLGB:** The **.bed** files for training and testing our circLGB model  
* **circMRT:** The **.bed (.fasta)** files for training and testing our circMRT model  
#### **features**   
* **circLGB:** Sequence-derived features of the given sequences for circRNA identification    
* **circMRT:** Sequence-derived features of the query sequences for circRNA regulatory interactions prediction  
* **feature_importance:** Ranked feature list for circLGB and circMRT  
#### **weights**   
* The well-trained weights for circLGB & circMRT models        
#### **circLGB.py & circMRT.py**   
* The Python codes, they can be ran to reproduce our predictors results
#### **result**     
* The prediction results of our predictors on the test data    
#### **Note:**    
  The **features/circLGB/test.csv** and **features/circMRT/test.csv** can replaced or modified to the sequence-derived features of interest for identifying circular RNA and predicting its regulatory interactions, respectively. 


## Testing circLGB with test set
python circLGB.py

## Testing circMRT with test set
python circMRT.py


