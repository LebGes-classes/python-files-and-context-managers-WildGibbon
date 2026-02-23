from HomeWork.FileManagement.Serialization.IItemCatalogSerializer import IItemCatalogSerializer


class JsonItemCatalogSerializer(IItemCatalogSerializer):
    def serialize(self, item_catalog):
        items = []

        for item in item_catalog.get_items():
            items.append({'name': item.get_name(),
                          'quantity': item.get_quantity(),
                          'state': item.get_state().value,
                          'supplier': item.get_supplier(),
                          'manufacturer': item.get_manufacturer(),
                          'price': item.get_price(),
                          'location': item.get_location(),
                          'city': item.get_city(),
                          'product_id': item.get_item_id()})

        return {"items": items}
