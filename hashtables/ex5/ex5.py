# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    file_table = {}

    for file in files:
        file_array = file.split("/")
        file_name = file_array[len(file_array)-1]
        if file_name not in file_table:
            file_table[file_name] = [file]
        else:
            file_table[file_name].append(file)

    for query in queries:
        if query in file_table:
            result.extend(file_table[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "bar"
    ]
    print(finder(files, queries))
