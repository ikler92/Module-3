def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return


list_ = [1, 2, 3]
print_params()
print_params(*list_)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [4, "строчка", 6.5]
values_dict = {'a': True, 'b': 15, 'c': 1.72}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
