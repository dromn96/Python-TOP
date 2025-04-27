def count_arr(list):
    sum = 0
    count = 0
    for i in range(len(list)):
        if i % 2 == 0 or i == 0:
            sum += list[i]
            count = sum * list[-1]
    return count

print(count_arr([0, 1, 2, 3, 4, 5]))
print(count_arr([1, 3, 5]))
print(count_arr([6]))
print(count_arr([]))