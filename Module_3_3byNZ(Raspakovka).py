def print_params(a=1, b='строка', c=True):  # *args, **kwargs
    print(a, b, c)
    print()


print_params(1, 'строка', True)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [4, 'slovo', False]
values_dict = {'a': 7, 'b': 'vстрока', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [45.65, True]
print_params(*values_list_2, 'пять')
