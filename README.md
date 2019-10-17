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
* **./features/circLGB/test.csv:** The testing examples with 191 sequence-derived features and label indicating the type of RNA    
* **./weights/circLGB.txt:** The well-trained weights for circLGB model      
* **./circLGB.py:** The Python code, it can be ran to reproduce our circLGB results  
* **./result/circLGB_test_result.csv:** The prediction results of circLGB on the test data 
#### **Note:**    
The test.csv can replaced or modified to 191 sequence features of interest  

## Testing circLGB with test set
python circLGB.py

## Testing circMRT with test set
python circMRT.py


