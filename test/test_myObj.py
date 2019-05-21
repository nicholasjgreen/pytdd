from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
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
        self.assertEqual(60, obj.add_from_repo())

    @patch('src.MyRepo.MyRepo')
    def test_add_from_repo_with_patching(self, mock_repo):
        repo = mock_repo()
        print(repo.get_data())
        repo.get_data = MagicMock(return_value=[10, 20, 30])
        self.assertEqual([10, 20, 30], repo.get_data())

    def test_add_from_repo_with_context_manager(self):
        with patch.object(MyRepo, 'get_data', return_value=[10, 20, 30]) as patched_repo:
            # When we create a repo we now get the patched mock instead
            repo = MyRepo()
            self.assertEqual([10, 20, 30], repo.get_data())

            # You can check that the patched method was called
            patched_repo.assert_called()

            # We can pass this into constructors
            obj = MyObj(repo)
            self.assertEqual(60, obj.add_from_repo())

            # Also works when something else (within this context) creates a repo
            obj = MyObj()   # When None is passed into constructor it will create its own MyRepo
            self.assertEqual(60, obj.add_from_repo())
