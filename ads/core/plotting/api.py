import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix


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
    



def plot_decision_regions(X, y, classifier, resolution=0.02, test_idx=None, xlabel='feature1',
                            ylabel='feature2', title=None, legend=None):
    """
    Conveinience function to visualize the decision boundaries
    for two-dimensional datasets
    """
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), 
                            np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    if legend:
        plt.legend()

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0], X_test[:, 1],
                    c='', edgecolor='black', alpha=1.0,
                    linewidth=1, marker='o',
                    s=100, label='test set')
    plt.show()


def plot_linear(X, y, model):
    plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
    plt.plot(X, model.predict(X), color='black', lw=2)
    plt.show()