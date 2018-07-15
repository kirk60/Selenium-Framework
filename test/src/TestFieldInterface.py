import unittest
from LocalLib.FieldInterface import FieldInterface


class MockFieldInterface(FieldInterface):
    _get_value = None

    def set_get_value(self, value):
        self._get_value = value

    def get_value(self):
        if self._get_value is None:
            self.raise_not_found()
        return self._get_value


class TestFieldInterface(unittest.TestCase):

    def test_constructor(self):
        """
        Basic Constructor test
        :return:
        """
        name = "fred"
        a = FieldInterface(name)
        self.assertEqual(name, a.name)
        self.assertIsNone(a.error)
        self.assertIsNone(a.get_error())

    def test_get_raise_error(self):
        field = FieldInterface('fred')
        with self.assertRaises(NotImplementedError):
            field.get_value()

    def test_is_valid_raise_error(self):
        field = FieldInterface('fred')
        with self.assertRaises(NotImplementedError):
            field.is_valid()

    def test_dummy_get_value_found(self):
        field = MockFieldInterface('fred')
        field.set_get_value('boris')
        self.assertEqual('boris', field.get_value())
        self.assertTrue(field.is_valid())

    def test_dummy_get_value_not_found(self):
        field = MockFieldInterface('fred')
        field.set_get_value(None)
        self.assertFalse(field.is_valid())


if __name__ == '__main__':
    unittest.main()
