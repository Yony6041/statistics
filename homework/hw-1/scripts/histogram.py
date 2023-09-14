import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import os

# Global variable to keep track of the last used filename
last_used_index = -1

def plot_frequencies_and_distribution(data, bins=60, xlim=(-4, 4)):
    
    global last_used_index
    """
    This function takes a pandas Series or a list-like object and plots both a histogram
    and a distribution plot.
    
    Parameters:
    - data: The data to be plotted (pandas Series or list-like object)
    - bins: Number of bins for the histogram (default is 60)
    - xlim: x-axis limits for the histogram plot (default is (-4, 4))
    
    Returns:
    - None (plots will be displayed)
    """
    
    # Plotting the histogram
    plt.figure(figsize=(10, 7))
    plt.hist(data, bins=bins, color='blue', alpha=0.5, edgecolor='black')
    plt.title('Histograma de la muestra.')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.xlim(xlim)
    plt.grid(axis='y', alpha=0.75)
    
    last_used_index += 1
    filename_letter = string.ascii_lowercase[last_used_index % 26]
    
    # Check if the directory exists, if not, create it
    if not os.path.exists('../results'):
        os.makedirs('../results')
    
    plt.savefig(f'../results/relativeFrequency-{filename_letter}.png')
    plt.clf()
    
    # Plotting the distribution plot using seaborn
    sns.distplot(data)
    
    # Store sns plot in a file as well
    plt.savefig(f'../results/snsDistributionPlot-{filename_letter}.png')
    
    plt.clf()
