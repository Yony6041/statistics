# Importing required modules
from scipy.stats import skew, kurtosis

def calculate_symmetry(data):
    """
    This function calculates and prints the skewness and kurtosis of a given data array.
    
    Parameters:
    - data (list or array): The data for which to calculate skewness and kurtosis.
    
    Returns:
    - None: The function prints the skewness and kurtosis but does not return any value.
    """
    
    # Calculate Skewness
    # Skewness quantifies the extent and direction of skew (departure from horizontal symmetry) in the data.
    skewness = skew(data)
    
    # Calculate Kurtosis
    # Kurtosis quantifies whether the data is heavy-tailed or light-tailed relative to a normal distribution.
    kurt = kurtosis(data)
    
    # Displaying the calculated skewness and kurtosis
    print(f"Skewness of the data: {skewness}")
    print(f"Kurtosis of the data: {kurt}")

# Example usage:
# data = [31, 35, 37, 40, 40, 51, 54, 55, 57, 58, 60, 60, 62, 62, 65, 67, 75, 89]
# calculateSymmetry(data)
