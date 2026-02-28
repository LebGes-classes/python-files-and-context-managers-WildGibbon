from abc import ABC, abstractmethod
from typing import Any
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog


class IItemCatalogSerializer(ABC):
    """
    Абстрактный базовый класс для сериализации каталога товаров.
    """
    @abstractmethod
    def serialize(self, item_catalog: ItemCatalog) -> Any:
        """
        Абстрактный метод для сериализации каталога товаров.

        Args:
            item_catalog (ItemCatalog): Каталог товаров для сериализации.
        """
        pass
