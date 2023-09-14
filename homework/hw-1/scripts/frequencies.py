import numpy as np
import matplotlib.pyplot as plt
import string
import os
from typing import List, Union

# Global variable to keep track of the last used filename
last_used_index = -1

def count_grades_less_equal_than_x(x:int, grade_list: Union[int, float]) -> int:
    """
    Count the number of grades in a list that are less than or equal to a given value.
    """
    filtered_grades = [u for u in grade_list if u <= x]
    return len(filtered_grades)

def calculate_relative_frequency(x: int, grade_list: Union[int, float], n: int) -> float:
    """
    Calculate the relative frequency of grades that are less than or equal to a given value.
    """
    count = count_grades_less_equal_than_x(x, grade_list)
    return count / n

def calculate_frequencies(grade_list: np.ndarray):
    global last_used_index
    
    values = sorted(set(grade_list))
    print("Sorted Grades:", sorted(values))

    grades_dict = {"x_" + str(i + 1): values[i] for i in range(len(values))}
    print("Grades Dictionary:", grades_dict)

    frequencies = {"g_" + str(i + 1): np.count_nonzero(np.array(grade_list) == values[i]) for i in range(len(values))}
    print("Frequencies:", frequencies)
    print("Sum of Frequencies:", sum(frequencies.values()))

    x = [0+0.01*n for n in range(0,10000)]
    plt.plot(x, [calculate_relative_frequency(i, grade_list, len(grade_list)) for i in x])
    plt.xlim(0, 100)
    plt.ylim(0,1)
    
    last_used_index += 1
    filename_letter = string.ascii_lowercase[last_used_index % 26]
    
    # Check if the directory exists, if not, create it
    if not os.path.exists('../results'):
        os.makedirs('../results')
    
    plt.savefig(f'../results/relativeFrequency-{filename_letter}.png')
    plt.clf()
    
    print("The graph of the relative frequencies can be found in the results directory!")
