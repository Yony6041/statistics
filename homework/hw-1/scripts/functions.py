    
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