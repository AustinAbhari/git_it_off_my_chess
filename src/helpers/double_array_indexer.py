def double_array_indexer(double_array, index):
    if type(index) is list:
        return double_array[index[0]][index[1]]

    if isinstance(index, str):
        index.replace("-", "")
        return double_array[int(index[0:1])][int(index[-1])]
