from functools import reduce
from src.MyRepo import MyRepo


class MyObj:
    def __init__(self, repo=None):
        self.repo = repo or MyRepo()

    def add_from_repo(self):
        data = self.repo.get_data()
        return reduce(lambda x, y: x+y, data)

