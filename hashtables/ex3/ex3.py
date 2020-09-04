def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    insec_table = {}
    result = []
    for array in arrays:
        for number in array:
            if number not in insec_table:
                insec_table[number] = 1
            else:
                insec_table[number] += 1

    for number in insec_table:
        if insec_table[number] > 1:
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
