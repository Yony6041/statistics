import numpy as np
import matplotlib.pyplot as plt

"""
Count the number of grades in a list that are less than or equal to a given value.

Parameters:
- x (int or float): The value to compare each grade against.
- grade_list (list): The list of grades to be counted.

Returns:
- int: The number of grades that are less than or equal to x.
"""
def count_grades_less_equal_than_x(x:int, list: [int]):
   
    # Use a list comprehension to filter grades that are less than or equal to x
    filtered_grades = [u for u in list if u <= x]
    
    # Return the length of the filtered list, which is the count of grades less than or equal to x
    return len(filtered_grades)

"""
Calculate the relative frequency of grades that are less than or equal to a given value.

Parameters:
- x (int or float): The value to compare each grade against.
- grade_list (list): The list of grades to be counted.
- n (int): The total number of grades in the list.

Returns:
- float: The relative frequency of grades that are less than or equal to x.
"""
def calculate_relative_frequency(x: int, list: list[int], n: int):
    # Use the count_grades_less_equal_than_x function to get the count of grades less than or equal to x
    count = count_grades_less_equal_than_x(x, list)
    
    # Calculate and return the relative frequency
    return count / n


def getFrecuencies(list: np.ndarray):
    # Sort and remove duplicates
    values = sorted(set(list))

    # Display sorted grades
    print("Sorted Grades:", sorted(values))

    # Create a dictionary with sorted grades
    grades_dict = {"x_" + str(i + 1): values[i] for i in range(len(values))}
    print("Grades Dictionary:", grades_dict)

    # Create a dictionary with frequencies of each grade
    frequencies = {"g_" + str(i + 1): np.count_nonzero(np.array(list) == values[i]) for i in range(len(values))}
    print("Frequencies:", frequencies)

    # Sum of frequencies (should match the length of the original list)
    print("Sum of Frequencies:", sum(frequencies.values()))

    # Plot the relative frecuency of the elements in the list

    x = [0+0.01*n for n in range(0,10000)]
    plt.plot(x, [calculate_relative_frequency(i, list, len(list)) for i in x])
    plt.xlim(0, 100)  # or any value greater than 89
    plt.ylim(0,1)
    plt.savefig('../results/relativeFrequency-a.png')
    print("The graph of the relative frequencies can be found in the results directory!")