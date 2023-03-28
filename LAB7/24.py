"""
Author :
Srihari K G - 210030035
Tejas - 210030039 
Indian Institute of Technology Dharwad
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def chooseBestFeature(df):
    """
    From the given dataframe selects the root node
    """
    categorical = df.columns[-1]
    
    feature_array = df.columns[:-1]
    
    ig_array = dict()
    
    for i in feature_array:
        ig_array[i] = getInfoGainOverFeature(df,i)
        
    return max(ig_array, key=ig_array.get),ig_array[max(ig_array, key=ig_array.get)]   

def getInfoGainOverFeature(df,feature):
    
    """
    Return the information gain for a given part of dataframe
    on splitting upon a feature
    """
    categorical = df.columns[-1]
    
    
    dataframe_array = []

    for value in df[feature].unique():
        dataframe_array.append(df[df[feature]==value])
    
    feature_dict = dict()
    entropy_array = []
    
    for dataframe in dataframe_array:
        entropy_array.append(entropy(dataframe))
        
    
    entropy_parent = entropy(df)
    
    total_values = len(df)
    
    factor_array = []
    for i in range(len(entropy_array)):
        factor_array.append( ((len(dataframe_array[i])/total_values))*entropy_array[i] )
    
    return entropy_parent-sum(factor_array)
    

def mylog(num):
    """
    Returns log base 2 of number
    """
    if num!=0 :
        return np.log2(num)
    return 0


def entropy(df):
    """
    Returns entropy of a part of dataframe
    """
    categorical = df.columns[-1]
    count = dict()
    for  x in df[categorical].unique():
        count[x]=0
    for  x in df[categorical].values:
        count[x]+=1

    total_Values = len(df[categorical].values) 
    
    return -1*sum([(count[i]/total_Values)*mylog(count[i]/total_Values) for i in count.keys() ])


def generateTree(df,depth):

    if (len(df[df.columns[-1]].unique())==1) or (depth==0):
        return (df[df.columns[-1]].unique())[0]
    
    else:
        best_feature , info_gain = chooseBestFeature(df)
        tree = {best_feature : {}}
        
        for i in df[best_feature].unique():
            tree[best_feature][i] = generateTree(df[df[best_feature]==i],depth-1)
        return tree   


if __name__ == '__main__':
    file_name = sys.argv[1]
    df = pd.read_table(file_name)
    max_depth = 5
    tree = generateTree(df,max_depth)

    print("Decision Tree")
    print(tree)