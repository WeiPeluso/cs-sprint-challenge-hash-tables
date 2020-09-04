def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    number_table = {}
    result = []

    for number in a:
        if abs(number) in number_table:
            result.append(abs(number))
        else:
            number_table[abs(number)] = abs(number)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
