import numpy as np


def outliers(data, Q_1, Q_3, IQR):
  return [x for x in sorted(data) if x<Q_1-3*IQR/2 or x>Q_3+3*IQR/2]

def no_outliers(data, Q_1, Q_3, IQR):
  return [x for x in data if x not in outliers(data, Q_1, Q_3, IQR)]



def percentile(data, p):
  return np.nanquantile(data, float(p))


def quantile(data):
  
    sorted_data = sorted(data)
    
    # Calculate the first quartile (Q1) using np.percentile()
    Q1 = percentile(sorted_data, 0.25)
    
    # Calculate the second quartile (Q2) using np.percentile()
    Q2 = percentile(sorted_data, 0.50)
    
    # Calculate the third quartile (Q3) using np.percentile()
    Q3 = percentile(sorted_data, 0.75)
    
    # Calculate the interquartile range (IQR)
    IQR = Q3 - Q1
    return Q1, Q2, Q3, IQR


def calculate_centralTendency(sample_data: np.ndarray):
    """
    Calculate and print the sample mean, sample median, and quartiles of a given NumPy array.
    
    Parameters:
    - sample_data (numpy.ndarray): The sample data as a NumPy array.
    
    Returns:
    - None: This function prints the sample mean, sample median, and quartiles.
    """
    
    # Calculate the sample mean using np.mean()
    sample_mean = np.mean(sample_data)
    
    # Calculate the sample median using np.median()
    sample_median = np.median(sample_data)

    Q1, Q2, Q3, IQR = quantile(sample_data)
    
    
    # Calculate Atypical values
    listOutliers = outliers(sample_data, Q1, Q3, IQR)
    listWithoutOutliers = no_outliers(sample_data, Q1, Q3, IQR)
    return sample_mean, sample_median, Q1, Q2, Q3, IQR, listOutliers, listWithoutOutliers
    
    # Print the results
    print(f"Sample Mean: {sample_mean}")
    print(f"Sample Median: {sample_median}")
    print(f"First Quartile (Q1): {Q1}")
    print(f"Second Quartile (Q2): {Q2}")
    print(f"Third Quartile (Q3): {Q3}")
    print(f"Interquartile Range (IQR): {IQR}")
    print(f"Outliers: {listOutliers}")
    print(f"Without Outliers: {listWithoutOutliers}")
