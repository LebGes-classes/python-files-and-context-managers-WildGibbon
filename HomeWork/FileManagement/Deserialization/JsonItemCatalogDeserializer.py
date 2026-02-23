import json

from HomeWork.FileManagement.Deserialization.IItemCatalogDeserializer import IItemCatalogDeserializer
from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog


class JsonItemCatalogDeserializer(IItemCatalogDeserializer):
    def deserialize(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items = []

            for item_data in data['items']:
                item_data['state'] = ItemState(item_data['state'])
                item = Item(**item_data)
                items.append(item)

            return ItemCatalog(items)
