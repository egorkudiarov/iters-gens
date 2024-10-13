class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        

    def flat_generator(self, _item):
        for item in iter(_item):
            if type(item) == list:
                self.flat_generator(item)
                continue
            self.flat_list.append(item)


    def __iter__(self):
        self.flat_list = []
        self.cursor = -1
        self.flat_generator(self.list_of_lists)
        return self

    def __next__(self):
        if self.cursor + 1 >= len(self.flat_list):
            raise StopIteration
        else:
            self.cursor += 1
            return self.flat_list[self.cursor]