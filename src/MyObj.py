from functools import reduce


class MyObj:
    def __init__(self, repo):
        self.repo = repo

    def add_from_repo(self):
        data = self.repo.get_data()
        return reduce(lambda x, y: x+y, data) % 10

