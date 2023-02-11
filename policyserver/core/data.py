import sys
import os
import json


class DataLoader(object):
    def __init__(self, rules_root):
        self.rules_root = rules_root
        sys.path.append(rules_root)

    def read_data(self, file_name):
        with open(self.rules_root + "/" + file_name) as f:
            return json.load(f)

    def get_data_name(self):
        return [rule for rule in os.listdir(self.rules_root) if rule.endswith(".json")]

    def load_data(self):
        final_data = {}
        for data_file in self.get_data_name():
            data = self.read_data(data_file)
            final_data.update({data_file.replace(".json", ""): data})
        return final_data
