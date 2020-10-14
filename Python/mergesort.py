def merge_sorted_lists(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    index1 = 0
    index2 = 0
    result = []

    while index1 < length1 and index2 < length2:
        if list1[index1] <= list2[index2]:
            result.append(list1[index1])
            index1 += 1
        else:
            result.append(list2[index2])
            index2 += 1

    if index1 == length1:
        while index2 < length2:
            result.append(list2[index2])
            index2 += 1

    if index2 == length2:
        while index1 < length1:
            result.append(list1[index1])
            index1 += 1

    return result

def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list

    middle = int(len(input_list) / 2)
    list1 = input_list[:middle]
    list2 = input_list[middle:]

    left = mergesort(list1)
    right = mergesort(list2)

    return merge_sorted_lists(left, right)
