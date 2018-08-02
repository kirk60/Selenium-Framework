#############################################################################################
#
# Test FieldInterface :
#
# Copyright (C) 2018  Kirk Larson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################################


from LocalLib.FieldInterface import FieldInterface
import pytest


class MockFieldInterface(FieldInterface):
    _get_value = None

    def set_get_value(self, value):
        self._get_value = value

    def get_value(self , driver ):
        if self._get_value is None:
            self.raise_not_found()
        return self._get_value


def test_constructor():
    """
    Basic Constructor test
    :return:
    """
    name = "fred"
    a = FieldInterface(name)
    assert name == a.name
    assert a.error is None
    assert a.get_error() is None


def test_get_raise_error():
    field = FieldInterface('fred')
    with pytest.raises(NotImplementedError):
        field.get_value(None)


def test_is_valid_raise_error():
    field = FieldInterface('fred')
    with pytest.raises(NotImplementedError):
        field.is_valid(1)


def test_dummy_get_value_found():
    field = MockFieldInterface('fred')
    field.set_get_value('boris')
    assert 'boris' == field.get_value(1)
    assert field.is_valid(1)


def test_dummy_get_value_not_found():
    field = MockFieldInterface('fred')
    field.set_get_value(None)
    assert not field.is_valid(1)
