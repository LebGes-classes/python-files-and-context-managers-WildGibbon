import json


class FileManager:
    def save_json(self, json_data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
