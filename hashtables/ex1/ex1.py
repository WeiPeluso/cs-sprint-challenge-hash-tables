def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    number_table = {}
    index = 0
    if length == 1:
        return None
    while index < length:
        complement = limit - weights[index]
        if complement not in number_table:
            number_table[weights[index]] = index
            index += 1
        else:
            return [index, number_table[complement]]
