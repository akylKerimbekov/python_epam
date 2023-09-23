from random import randint


def generate_list() -> list:
    """
    Generates a list of 100 random integers ranging from 0 to 1000.
    """
    return [randint(0, 1000) for _ in range(100)]


def sorting(raw: list) -> list:
    """
    Sorts the given list in ascending order using the Bubble Sort algorithm.
    Args:
        raw (list): The original list to be sorted.
    Returns:
        list: A new list containing the sorted elements from the original list.
    """
    array = raw[:]
    array_length = len(array) - 1
    for i in range(0, array_length):
        for j in range(array_length):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def avg_even_odd(raw: list):
    """
    Calculates the average of even and odd numbers in the given list.
    Args:
        raw (list): The original list containing integers.
    Returns:
        tuple: A tuple containing two integers, the first one is the average
               of even numbers and the second one is the average of odd numbers.
    """
    even = 0
    odd = 0
    count = len(raw)
    for item in raw:
        if item % 2 == 0:
            even += item
        else:
            odd += item
    return even // count, odd // count


if __name__ == '__main__':
    # Generate a list of random integers.
    _list = generate_list()
    # Sort the list in ascending order.
    _sorted_list = sorting(_list)
    # Calculate the average of even and odd numbers in the sorted list.
    _avg_even_odd = avg_even_odd(_sorted_list)

    print(f'generated list: {_list}')
    print(f'sorted list: {_sorted_list}')
    print(f'average for even numbers: {_avg_even_odd[0]}, and for odd: {_avg_even_odd[1]}')
