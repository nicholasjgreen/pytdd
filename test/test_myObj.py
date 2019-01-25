from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
from src.MyRepo import *
from src.MyObj import *


class TestMyObj(TestCase):
    def test_add_from_repo(self):
        repo = MyRepo()
        obj = MyObj(repo)

        # Test against default values from repo. This assumes the test knows these default values
        self.assertEqual(1+2+3, obj.add_from_repo())

        # Mock in my own values, this means we control the input from inside the test
        # It is a monkey patch on the method, which is a bit gross
        repo.get_data = MagicMock(return_value=[10, 20, 30])
        self.assertEqual(0, obj.add_from_repo())

    @patch('src.MyRepo.MyRepo')
    def test_add_from_repo_with_patching(self, MockRepo):
        print(MockRepo.get_data())
        self.assertEqual([1, 2, 3], MockRepo.get_data())
