import pandas as pd


def prepros(data: dict):
    width = find_max_item(data) + 1
    height = len(data)

    li = get_init_list(height, width)

    for i in range(0, len(data)):
        for item in data[i]:
            li[i][item] = True

    return li


def find_max_item(data):
    max_item = 0
    for value in data:
        if max_item < max(list(value)):
            max_item = max(list(value))

    return max_item


def get_init_list(height, width):
    li = []
    for i in range(0, int(height)):
        row = []
        for j in range(0, int(width)):
            row.append(False)
        li.append(row)

    return li



