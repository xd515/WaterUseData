import os
import pandas as pd

def discribe(filename):
    '''
    Describe the features of the dataset.
    '''
    filename = str(filename)   
    if not os.path.exists(filename):
        raise FileNotFoundError("File %s does not exist."%filename)
        
    df = pd.read_csv(filename)
    shapes = df.shape
    columns = df.columns
    print("There are %s rows and %s columns displayed by the dataset."%shapes)
    print("Names of columns are: \n  %s"%"\n  ".join(columns))
    
    
def missings_report(filename):
    '''
    Describe the ompletence of the dataset.
    '''
    filename = str(filename)   
    if not os.path.exists(filename):
        raise FileNotFoundError("File %s does not exist."%filename)
        
    df = pd.read_csv(filename)
    columns = df.columns
    r = df.isnull().sum().sum()
    if r == 0:
        print('There is no null value in each column.')
    else:
        print('Caution: There are missing values in the dataset.')
        t = 1 - r/(df.shape[0]*df.shape[1])
        print("The completence of the whole dataset is {:.2%}.".format(t))
    
        for i in columns:
            a = df[i].isnull().sum()
            b = 1 - a/len(df[i])
            print("  '{}' : {:.2%}".format(i, b))
        