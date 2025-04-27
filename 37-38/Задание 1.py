def inversion(list_number):
    max = 0
    count = 0
    for i in list_number:
        if i > max:
            max = i
        else:
            count += 1
    return count

print(inversion([1, 2, 5, 3, 4, 7, 6]))