class ItemCatalogMenuView:
    def visualize(self, items):
        items_list = ""
        for i in range(len(items)):
            items_list += f"║ {i + 1}: {items[i].get_name()}".ljust(40) + "║\n"

        items_list += f"║ {len(items) + 1}: Добавить карточку".ljust(40) + "║\n"
        items_list += f"║ {len(items) + 2}: Удалить карточку".ljust(40) + "║\n"

        result = (f"╔═══════════════════════════════════════╗" + "\n" +
                  f"║ 0: Выйти                              ║" + "\n" +
                  items_list +
                  f"╠═══════════════════════════════════════╣" + "\n" +
                  f"║           ВЫБЕРИТЕ КАРТОЧКУ           ║" + "\n" +
                  f"╚═══════════════════════════════════════╝" + "\n")

        return result

