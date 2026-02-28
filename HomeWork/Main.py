from HomeWork.FileManagement.Deserialization.JsonItemCatalogDeserializer import JsonItemCatalogDeserializer
from HomeWork.FileManagement.Serialization.JsonItemCatalogSerializer import JsonItemCatalogSerializer
from HomeWork.FileManagement.FileManager.FileManager import FileManager
from HomeWork.ItemCatalog.ItemCatalogMenuView import ItemCatalogMenuView
from HomeWork.ItemCatalog.ItemCatalogMenu import ItemCatalogMenu
from HomeWork.Item.Menu.ItemMenu import ItemMenu
from HomeWork.Item.ItemView import ItemView

deserializer = JsonItemCatalogDeserializer()
serializer = JsonItemCatalogSerializer()
file_manager = FileManager()
file_path = "Data/my_data.json"

catalog = deserializer.deserialize(file_path)
item_menu = ItemMenu(ItemView())
catalog_menu = ItemCatalogMenu(catalog, ItemCatalogMenuView(), item_menu)

catalog_menu.open()

file_manager.save_json(serializer.serialize(catalog), file_path)
