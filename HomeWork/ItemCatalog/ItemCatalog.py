from HomeWork.Item.Item import Item


class ItemCatalog:
    def __init__(self, items: list[Item]):
        self.__items = items

    def get_items(self):
        return tuple(self.__items)

    def append(self, item):
        self.__items.append(item)

    def pop(self, index):
        self.__items.pop(index)
