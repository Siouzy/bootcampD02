def ft_filter(function_to_apply, list_of_inputs):
    new_list = []
    for elem in list_of_inputs:
        if function_to_apply(elem):
            new_list.append(elem)
    return new_list
