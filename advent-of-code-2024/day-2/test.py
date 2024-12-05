def slice_except_one(lst):
    result = []
    for i in range(len(lst)):
        result.append(lst[:i] + lst[i + 1 :])
    return result


my_list = [1, 2, 3, 4, 5]
print(slice_except_one(my_list))
