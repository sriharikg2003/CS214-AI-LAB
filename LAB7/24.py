
import pandas as pd
import numpy as np
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


def generateTree(df, depth):
    """
    Returns a decision tree as a dictionary
    """
    if (len(df[df.columns[-1]].unique()) == 1) or (depth == 0) or (len(df.columns) == 1):
        return (df[df.columns[-1]].mode())[0]

    else:
        best_feature, info_gain = chooseBestFeature(df)
        tree = {best_feature: {}}

        for i in df[best_feature].unique():
            tree[best_feature][i] = generateTree(df[df[best_feature] == i].drop(columns=[best_feature]), depth - 1)
        return tree

def predict(test, tree,arr):
    """
    Predicts an input instance to yes or no based on decision tree
    """
    if type(tree)==str:
        return tree
    
    feature = list(tree.keys())[0]
    if test[feature] in tree[feature]:
        subtree = tree[feature][test[feature]]
        return predict(test, subtree,arr)
    else:
        return arr[-1]

def printTree(tree, gap=''):
    """
    Prints the decision tree in a readable format
    """
    if type(tree) == str:
        print(tree)
    else:
        for feature, subtree in tree.items():
            print(f'{gap}  {feature}:')
            for value, subsubtree in subtree.items():
                print(f'{gap*2}  {value} --> ', end='')
                printTree(subsubtree, gap + "  ")


def accuracy(df):
    """
    Returns the accuracy percentage
    """
    predicted = []
    for i in range(len(df)):
        predicted.append(predict(df.iloc[i],tree,df[df.columns[-1]].unique()))
    accuracy = 0
    actual = np.array(df[df.columns[-1]])

    accuracy = (sum(predicted == actual))*100/len(predicted)
    print(f"Total instances          :   {len(predicted)}")
    print(f"Correct Predicitions     :   {sum(predicted == actual)}")
    print(f"Inorrect Predicitions    :   {len(predicted)-sum(predicted == actual)}")
    print(f"Accuracy                 :   {accuracy} %")
    return 






if __name__ == "__main__":

    file_name = sys.argv[1]
    df = pd.read_table(file_name)

    max_depth = 10

    tree = generateTree(df,max_depth)
    print("Decision tree  : \n")
    printTree( tree)
    accuracy(df)

# .....
