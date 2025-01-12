import pandas as pd


class Database:
    def __init__(self, path):
        self.path = path
        self.content = self.import_database(self.path)

    def import_database(self, path) -> object:
        database_from_excel = pd.read_excel(path)
        return database_from_excel