def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 2)
print_params(a = 5, b = 55, c = 45)
print_params(c = [1, 2, 3])

values_list = [1, 'git', False]
values_dict = {'a': 19, 'b': 'Kolya', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [66, 'sata']
print_params(*values_list_2, 42)