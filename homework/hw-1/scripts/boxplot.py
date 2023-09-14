import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
import string
import os

# Global variable to keep track of the last used filename
last_used_index = -1

def plot_boxplots(data_0):
    global last_used_index
    """
    This function takes a pandas Series or a list-like object and plots both Matplotlib and Seaborn boxplots.
    
    Parameters:
    - data_0: The data to be plotted (pandas Series or list-like object)
    
    Returns:
    - None (plots will be displayed)
    """
    
    # Suppress warnings for better readability
    warnings.filterwarnings("ignore")
    
    # Using Matplotlib for boxplot
    plt.figure(figsize=(10, 7))
    plt.boxplot(data_0)
    plt.title('Matplotlib Boxplot')
    plt.xlabel('Box')
    plt.ylabel('Value')
    
    
    last_used_index += 1
    filename_letter = string.ascii_lowercase[last_used_index % 26]
    
    # Check if the directory exists, if not, create it
    if not os.path.exists('../results'):
        os.makedirs('../results')
    
    plt.savefig(f'../results/boxplot-{filename_letter}.png')
    plt.clf()
    
    # Using Seaborn for boxplot
    plt.figure(figsize=(10, 7))
    sns.boxplot(data=data_0)
    plt.title('Seaborn Boxplot')
    plt.xlabel('Box')
    plt.ylabel('Value')
    
    plt.savefig(f'../results/sns_boxplot-{filename_letter}.png')
    plt.clf()


