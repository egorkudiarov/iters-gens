def flat_generator(list_of_lists):
    flat_list = []
    for item in iter(list_of_lists):
        if type(item) == list:
            flat_list += [_ for _ in flat_generator(item)]
            continue
        flat_list.append(item)

    for cursor in range(len(flat_list)): 
        yield flat_list[cursor]