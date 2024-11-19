immutable_var = 1, 2, 3, True, 'apple'
print(immutable_var)
# immutable_var[1] = 5 - (кортеж, не поддерживает обращение по элементам)
mutable_list = [5, 6, 3, False, 'banana', 6]
mutable_list [3] = True
mutable_list [0] = 1
mutable_list [1] = 2
mutable_list [2] = 3
mutable_list [4] = 'apple'
mutable_list.remove(6)
print(mutable_list)