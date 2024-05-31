def flattened_array(arr):
    flattened = []
    for item in arr:
        if isinstance(item, list):
            flattened.extend(flattened_array(item))
        else:
            flattened.append(item)
    return flattened


a = [1,[2,3], [4,[5,[6,[7,8]]]]]
print(flattened_array(a))