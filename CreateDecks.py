

def generate_list(number, count):
    return [number] * count


def generate_multiple_lists(num_lists):
    # Create a dictionary to hold the generated lists
    all_lists = {}
    
    # Generate lists of four numbers
    for i in range(num_lists):
        current_list = []
        for j in range(2, 12):
            if j == 10:
                current_list += [10] * 16
            else:
                current_list += generate_list(j, 1) * 4
        all_lists[i] = current_list
    
    return all_lists



def shuffle_lists_in_dict(dict_of_lists):
    import random
    for key in dict_of_lists:
        random.shuffle(dict_of_lists[key])
    return dict_of_lists
