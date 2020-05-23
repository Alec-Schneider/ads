import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_confusion_matrix(y_true, predictions, title=None, figsize=(8,8), cmap='icefire'):
    """
    
    """
    plt.figure(figsize=figsize)
    sns.heatmap(confusion_matrix(y_true, predictions), annot=True, fmt='d', cmap=cmap)
    
    if title:
        plt.title(title)
    plt.xlabel('Actual Class')
    plt.ylabel('Predicted Class')
    plt.show()
    

def plot_predictions(y_true, predictions, title=None, figsize=(8,8), save_to=None):
    """
    """
    plt.figure(figsize=figsize)
    plt.scatter(predictions, y_true)
    
    if title:
        plt.title(title)
    plt.xlabel('Predicted Values')
    plt.ylabel('Actual Values')
    if save_to:
        plt.savefig(save_to)
    plt.show()
    
    
def plot_decision_boundary(classifier):
    """
    Plot the decision boundary of a classification model
    
    
    
    
    """
    
    pass 
    #plt.show()