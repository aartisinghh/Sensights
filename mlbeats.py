'''
This file will be used to store useful functions that can be used in the jupiter notebooks

'''
import pandas as pd
    

    
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


def window(df):
    '''
    Input: the middle of a given ecg signal, df is the signal that is being used
    Output: a sub array showing a single heartbeat which can have its features selected
    '''
    
    #dx is the distance that we will take from the centre of the wave
    dx = 50
    
    print("Hello")
    
    return wind
