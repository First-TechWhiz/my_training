def print_params(a = 1, b = 'strings', c = True):
    print(a, b, c)

#1
print_params(100, 200, 300)
print_params(b=25)
print_params(c=[1, 2, 3])

#2
values_list = [100, 'not_string', True]
values_dict = {"a": values_list[0], "b": values_list[1], "c": values_list[2]}
print_params(*values_list)
print_params(**values_dict)

#3
value_list_2 = ['Hello', 996]
print_params(*value_list_2, 42)