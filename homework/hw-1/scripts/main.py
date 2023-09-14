import pandas as pd
import numpy as np

from scipy.stats import skew, kurtosis
from frequencies import *
from centralTendency import *
from measuresOfDispersion import *
from measuresOfSymmetry import *







# Question a
print("==================================================")
print("==========           Solving question a           ==========")
print("==================================================")


# Original list of student grades
studentGrades = [31, 35, 37, 40, 40, 51, 54, 55, 57, 58, 60, 60, 62, 62, 65, 67, 75, 89]

calculate_frequencies(studentGrades)

sample_mean, sample_median, Q1, Q2, Q3, IQR, listOutliers, listWithoutOutliers = calculate_centralTendency(studentGrades)


print("Calculating dispersion in list with outliers:", listWithoutOutliers)
calculate_dispersion(studentGrades)
print("Calculating dispersion in list without outliers:", listWithoutOutliers)
calculate_dispersion(listWithoutOutliers)

print("Calculating symmetry in list with outliers:", studentGrades)
calculate_symmetry(studentGrades)

print("Calculating symmetry in list without outliers:", listWithoutOutliers)
calculate_symmetry(listWithoutOutliers)


# Question b
print("==================================================")
print("==========           Solving question b           ==========")
print("==================================================")



# Lost labour days in a company in a given month

lostLabourDays=  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 8, 45]

calculate_frequencies(lostLabourDays)

sample_mean, sample_median, Q1, Q2, Q3, IQR, listOutliers, listWithoutOutliers = calculate_centralTendency(lostLabourDays)


print("Calculating dispersion in list with outliers:", lostLabourDays)
calculate_dispersion(lostLabourDays)
print("Calculating dispersion in list without outliers:", listWithoutOutliers)
calculate_dispersion(listWithoutOutliers)

print("Calculating symmetry in list with outliers:", lostLabourDays)
calculate_symmetry(lostLabourDays)

print("Calculating symmetry in list without outliers:", listWithoutOutliers)
calculate_symmetry(listWithoutOutliers)





# Question c

print("==================================================")
print("==========           Solving question c           ==========")
print("==================================================")

# Health to height ratio of 20 people

healthToHeightRatio= [1.52, 1.60, 1.57, 1.52, 1.60, 1.75, 1.73, 1.63, 1.55, 1.63, 1.65, 1.55, 1.65, 1.60, 1.68 , 2.50, 1.52, 1.65, 1.60, 1.65]

calculate_frequencies(healthToHeightRatio)

sample_mean, sample_median, Q1, Q2, Q3, IQR, listOutliers, listWithoutOutliers = calculate_centralTendency(healthToHeightRatio)


print("Calculating dispersion in list with outliers:", healthToHeightRatio)
calculate_dispersion(healthToHeightRatio)
print("Calculating dispersion in list without outliers:", listWithoutOutliers)
calculate_dispersion(listWithoutOutliers)

print("Calculating symmetry in list with outliers:", healthToHeightRatio)
calculate_symmetry(healthToHeightRatio)

print("Calculating symmetry in list without outliers:", listWithoutOutliers)
calculate_symmetry(listWithoutOutliers)





# Question d
print("==================================================")
print("==========           Solving question d           ==========")
print("==================================================")

mtcars_df = pd.read_csv("../data/mtcars.csv")
# Loop through each column in the DataFrame to perform calculations
for column in mtcars_df.columns:
    print(f"Analyzing column: {column}")
    
    # Calculating frequencies
    print("Calculating frequencies:")
    calculate_frequencies(mtcars_df[column])
    
    # Calculating central tendency
    print("Calculating central tendency:")
    sample_mean, sample_median, Q1, Q2, Q3, IQR, listOutliers, listWithoutOutliers = calculate_centralTendency(mtcars_df[column])
    
    # Calculating dispersion with and without outliers
    print("Calculating dispersion in list with outliers:")
    calculate_dispersion(mtcars_df[column])
    
    print("Calculating dispersion in list without outliers:")
    calculate_dispersion(listWithoutOutliers)
    
    # Calculating symmetry with and without outliers
    print("Calculating symmetry in list with outliers:")
    calculate_symmetry(mtcars_df[column])
    
    print("Calculating symmetry in list without outliers:")
    calculate_symmetry(listWithoutOutliers)


