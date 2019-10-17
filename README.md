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
* **data**   
  circLGB: Bed files for training and testing our circLGB model  
  circMRT: Bed and Fasta files for training and testing our circMRT model  
* **features**   
  circLGB: 191-dimensional sequence-derived features of the given sequence for circRNA identification    
  circMRT: 182-dimensional sequence-derived features of the given sequence for circRNA regulatory interactions prediction  
  feature_importance: Ranked feature list for circLGB and circMRT  
* **weights:**   
  The well-trained weights for circLGB & circMRT models        
* **circLGB.py & circMRT.py:**   
  The Python codes, they can be ran to reproduce our predictors results
* **result**     
  The prediction results of our predictors on the test data    
#### **Note:**    
1. The features/circLGB/test.csv can replaced or modified to 191 sequence-derived features of interest for circRNA identification. 
2. The features/circMRT/test.csv can replaced or modified to 182 sequence-derived features of interest for circRNA regulatory interaction prediction

## Testing circLGB with test set
python circLGB.py

## Testing circMRT with test set
python circMRT.py


