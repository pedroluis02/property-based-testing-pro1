import random

from quicksort import quicksort


def generate_int_values(length=1, max_value=1000):
    assert length > 0, f'length greater than 0 expected, got {length}'
    assert max_value > 0,  f'max_value greater than 0 expected, got {max_value}'

    new_list = []
    for i in range(0, length):
        n = random.randint(1, max_value)
        new_list.append(n)
    return new_list


if __name__ == '__main__':
    print('Sort values')
    values = generate_int_values(10)
    print(f'unordered: {values}')

    quicksort(values)
    print(f'ordered: {values}')
