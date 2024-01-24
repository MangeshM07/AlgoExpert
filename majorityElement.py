def majorityElement(array):
    answer = None
    count = 0

    for value in array:
        if count == 0:
            answer = value

        if value == answer:
            count += 1
        else:
            count -= 1

    return answer


array = [1,2,2,7,2,2]
print(majorityElement(array))