import numpy as np

def calculate_dispersion(data):
    
    if len(data) == 0:
        print("The data array is empty. Cannot perform calculations.")
        return
    
    if len(data) == 1:
        print("The data array contains a single element. Variance and standard deviation will be zero.")
        print("Sample variance: 0")
        print("Sample standard deviation: 0")
        print("Sample range: Undefined")
        return
    
    # Sample variance
    variance = np.var(data)
    
    # Sample standard deviation
    standard_deviation = np.std(data)
    
    # Sample range
    sampleRange = np.amax(data) - np.amin(data)
    
    print("Sample variance:", variance)
    print("Sample standard deviation:", standard_deviation)
    print("Sample range:", sampleRange)
