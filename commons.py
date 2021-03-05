import pandas


def readcsv(filename):
    return pandas.read_csv(filename)


def remove_element_list(input_list, to_be_removed):
    return [elem for elem in input_list if elem != to_be_removed]