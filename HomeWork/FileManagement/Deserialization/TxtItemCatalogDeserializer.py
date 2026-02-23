from HomeWork.FileManagement.Deserialization.IItemCatalogDeserializer import IItemCatalogDeserializer
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog
from HomeWork.Item.Item import Item


class TxtItemCatalogDeserializer(IItemCatalogDeserializer):
    def deserialize(self, file_path):
        items = []

        with open(file_path, encoding='utf-8') as file:
            for row in file.read().splitlines():
                data = row.split(';')
                item = Item(
                    data[1],
                    int(data[2]),
                    int(data[3]),
                    data[4],
                    data[5],
                    int(data[6]),
                    data[7],
                    data[8],
                    data[0],
                )

                items.append(item)

        return ItemCatalog(items)
