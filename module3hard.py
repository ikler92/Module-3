data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def sum_numbers(data_structure):
    if isinstance(data_structure, int):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, dict):
        summ = 0
        for key, value in data_structure.items():
            summ += sum_numbers(key)
            summ += sum_numbers(value)
        return summ
    elif hasattr(data_structure, '__iter__'):
        summary = 0
        for i in data_structure:
            summary += sum_numbers(i)
        return summary


print(sum_numbers(data_structure))
