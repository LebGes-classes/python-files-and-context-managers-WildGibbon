from abc import ABC, abstractmethod

from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog


class IItemCatalogSerializer(ABC):
    @abstractmethod
    def serialize(self, item_catalog: ItemCatalog):
        pass
