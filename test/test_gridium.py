import flask
import unittest

from app import gridium


class Test(unittest.TestCase):
    def test_app_is_exposed(self):
        self.assertIsInstance(gridium.app, flask.Flask)

if __name__ == '__main__':
    unittest.main()
