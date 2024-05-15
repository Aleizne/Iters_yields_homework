class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.ind_list = 0
        self.ind_item = 0
        return self

    def __next__(self):
        if self.ind_list >= len(self.list_of_list):
            raise StopIteration

        if self.ind_item >= len(self.list_of_list[self.ind_list]):
            self.ind_list += 1
            self.ind_item = 0
            return self.__next__()

        item = self.list_of_list[self.ind_list][self.ind_item]
        self.ind_item += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(list_of_lists_1):
        print(item)


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()
