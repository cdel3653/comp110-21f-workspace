"""Practice with dictionaries."""

__author__ = "730320843"


def flipper(input_dict):       
    invert = dict()

    for key in input_dict.keys():
        if input_dict[key] in invert:
            raise KeyError("non-unique key used.")
        else:
            invert[input_dict[key]] = key

    return invert


def favorite_color(i):
    color_frequency = dict()

    for key in i.keys():
        if i[key] not in color_frequency:
            color_frequency[i[key]] = 1   
        else:
            color_frequency[key] += 1

    maxval = 0

    for key in color_frequency.keys():
        if color_frequency[key] > maxval:
            maxval = color_frequency[key]

    maxlist = list()

    for key in color_frequency.keys():
        if color_frequency[key] == maxval:
            maxlist.append(key)

    first_max_color = ""

    for key in i.jeys():
        if i[key] in maxlist:
            first_max_color = i[key]
            break

    return first_max_color


def count(i):
    list_item_frequency = dict()
    
    for item in i:
        if item not in list_item_frequency:
            list_item_frequency[item] = 1
        else:
            list_item_frequency[item] += 1
        
    return list_item_frequency