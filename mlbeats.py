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



