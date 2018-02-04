import flask
import unittest

from app import gridium


class Test(unittest.TestCase):
    def test_app_is_exposed(self):
        self.assertIsInstance(gridium.app, flask.Flask)

    def test_get_bills(self):
        self.assertIsInstance(gridium.get_bills(), dict)

    def test_get_bills_data(self):
        self.assertIsInstance(gridium.get_bills()['data'], list)


if __name__ == '__main__':
    unittest.main()
