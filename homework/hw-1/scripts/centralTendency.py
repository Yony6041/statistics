import numpy as np

def calculate_and_print_statistics(list):
    """
    Calculate and print the sample mean and sample median of a given NumPy array.
    
    Parameters:
    - list (numpy.ndarray): The sample data as a NumPy array.
    
    Returns:
    - None: This function prints the sample mean and sample median.
    """
    
    # Calculate the sample mean using np.mean()
    sample_mean = np.mean(list)
    
    # Calculate the sample median using np.median()
    sample_median = np.median(list)
    
    # Print the results
    print(f"Sample Mean: {sample_mean}")
    print(f"Sample Median: {sample_median}")

