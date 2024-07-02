import pandas as pd
import numpy as np

data = pd.read_csv('file.csv')

def gini_impurity(y):
    if isinstance(y, pd.Series):
        p = y.value_counts()/y.shape[0]
        gini = 1 - np.sum(p**2)
        return (gini)
    else:
        raise ValueError('y must be a pandas Series')
    
gini_impurity(data['target'])

def entropy(y):
    if isinstance(y, pd.Series):
        a = y.value_counts()/y.shape[0]
        entropy = np.sum(-a*np.log2(a+1e-9))
        return (entropy)
    else:
        raise ValueError('y must be a pandas Series')

entropy(data['target'])

def variance(y):
    if(len(y) == 1):
        return 0
    else:
        return y.var()
    
def information_gain(y, mask, func=entropy):
    a = sum(mask)
    b = mask.shape[0] - a
    
    if (a == 0 or b == 0):
        ig = 0
    else:
        if y.dtypes != '0':
            ig = variance(y) - (a/(a+b) * variance (y[mask])) - (b / (a+b) * variance(y[-mask]))
        else:
            ig = func(y) - a / (a+b) * func(y[mask]) - b / (a+b) * func(y[-mask])
            
    return ig

information_gain(data['target1'], data['target2'] == 'target')

