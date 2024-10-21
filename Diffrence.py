def even_num_prod():
    num = 1
    for i in range(1, 21, 2):
        num *= i
    return num


def odd_num_prod():
    num = 1
    for i in range(1, 20, 2):
        num *= i
    return num


print(even_num_prod())
print(odd_num_prod())

result = even_num_prod() - odd_num_prod()

print(result)
