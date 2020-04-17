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
  The **features/circLGB/test.csv** and **features/circMRT/test.csv** can replaced or modified to the sequence-derived features of interest for identifying circRNA and predicting its regulatory interactions, respectively. 


## Testing circLGB with test set
python circLGB.py

## Testing circMRT with test set
python circMRT.py


## Webserver (Currently under construction)
We have also provided an easy-to-use circLGB website with graphical interface for general users with limited access to computing resources, which is freely accessible through http://www.circlgb.com. The following description gives a step-by-step instruction on how to use the webserver to get the prediction result. First, click the **START** button to be taken to the prediction page. Second, input the query sequence in the **Input** box and click the **Submit** button for prediction. Note: the input sequence should be in the **FASTA** format. Upon submitting the sequence, the software will extract the features for the given sequence from a server. It takes about five minutes for return the prediction result from the online result web page. Note that, the **help** page provides a detailed explanation of manual process. <Br/> 
As examples for using the web server, we present the prediction of hsa_circ_0000030.
* First, click the **START** button to be taken to the prediction page.
* Second, users need to **submit** the hsa_circ_0000030 sequence into the **input** box to make prediction.  
* Third, click the **Submit** button to upload hsa_circ_0000030 sequence.  
* Fourth, click the **Prediction** button for prediction. The web server will return the prediction result in the **Gray** box on the right when the job finished.  

<div align=center><img width="150" height="150" src="https://github.com/Peppags/circLGB-circMRT/blob/master/figure/figure.jpg"/></div>
