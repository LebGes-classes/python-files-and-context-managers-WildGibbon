from abc import ABC


class IItemCatalogDeserializer(ABC):
    @staticmethod
    def deserialize(self, file_path):
        pass
