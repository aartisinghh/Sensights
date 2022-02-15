'''
This file will be used to store useful functions that can be used in the jupiter notebooks
'''
import pandas as pd
import numpy as np
import pywt 


def df_from_txt(txt_path):
    '''
    Input: Path to the annotations.txt file 
    Output: Pandas dataframe with the first three columns of the text file ("Time", "Sample#", "Result")
    
    '''
    data = []
    with open(txt_path,'r') as data_file:
        for line in data_file:
            data.append(line.split()[:3])
    df = pd.DataFrame(data[1:], columns = ['Time', 'Sample#', 'Result'])
    return df




def data_from_csv(csv_path):
    '''
     Input: Path to the csv file 
    Output: Numpy array with "\'MLII\'"
    
    '''
    df = pd.read_csv(csv_path, 'r')
    return df["\'MLII\'"]





def normalize(data):
    '''
    Input: ECG data, pandas series or numpy array
    Output: Normalized ECG data
    
    '''
    mx = np.amax(data)
    mn = np.amin(data)

    return (data - mn)/(mx - mn)



def denoising(data):
    '''
    Input: ECG data 
    Output: Denoised ECG data using wavelet techique

    '''
    motherwave = "coif5"

    w = pywt.Wavelet(motherwave)
    maxlev = pywt.dwt_max_level(len(data), w.dec_len)

    threshold = 0.02
    coeffs = pywt.wavedec(data, motherwave, level = maxlev)
    for j in range(1, len(coeffs)):
        if j<=3:
            coeffs[j] = 0
        else:
            coeffs[j] = pywt.threshold(coeffs[j], threshold*max(coeffs[j]))

    datarec = pywt.waverec(coeffs, motherwave)
    
    
    return datarec


