from HomeWork.Item.Item import Item
from abc import ABC, abstractmethod


class IItemMenu(ABC):
    @abstractmethod
    def open(self, item: Item):
        pass
