import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
from frequencies import *
from frequencies import *

# Question a
print("Question a")

# Original list of student grades
studentGrades = [31, 35, 37, 40, 40, 51, 54, 55, 57, 58, 60, 60, 62, 62, 65, 67, 75, 89]

# Sort and remove duplicates
values = sorted(set(studentGrades))

# Display sorted grades
print("Sorted Grades:", sorted(values))

# Create a dictionary with sorted grades
grades_dict = {"x_" + str(i + 1): values[i] for i in range(len(values))}
print("Grades Dictionary:", grades_dict)

# Create a dictionary with frequencies of each grade
frequencies = {"g_" + str(i + 1): np.count_nonzero(np.array(studentGrades) == values[i]) for i in range(len(values))}
print("Frequencies:", frequencies)

# Sum of frequencies (should match the length of the original list)
print("Sum of Frequencies:", sum(frequencies.values()))

# Plot the relative frecuency of the elements in the list

x = [0+0.01*n for n in range(0,10000)]
plt.plot(x, [calculate_relative_frequency(i, studentGrades, len(studentGrades)) for i in x])
plt.xlim(0, 100)  # or any value greater than 89
plt.ylim(0,1)
plt.savefig('../results/relativeFrequency-a.png')
print("The graph of the relative frequencies can be found in the results directory!")

# Question b

# Question c

# Question d