from unittest import TestCase
from src.MyRepo import *
from src.MyObj import *

class TestMyObj(TestCase):
    def test_add_from_repo(self):
        repo = MyRepo()
        obj = MyObj(repo)

        self.assertEqual(1+2+3+4, obj.add_from_repo())
