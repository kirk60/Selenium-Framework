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
from LocalLib.FieldInterface import FieldNotFoundError
from selenium import webdriver

import pytest


class MockFieldInterface(FieldInterface):
    text = None

    def set_get_value(self, value , timeout = None):
        self.text = value

    def _get_element(self, driver:webdriver, reference=None,timeout:int=None):
    #
    #    The tests require that the return object implements a text
    #    field (like a Selenium element does :-)
    #
        if self.text == None:
            raise FieldNotFoundError("Error")
        return self


def test_constructor():
    """
    Basic Constructor testNone
    assert a.error is None
    assert a.get_error() is None


def test_get_raise_error():
    field = FieldInterface('fred')
    with pytest.raises(NoFieldNotFoundErrortImplementedError):
        field.get_value(None)


def test_is_valid_raise_error():
    field = FieldInterface('fred')
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
    
def test_timeout_init_none():
    '''
    Timeout is critical, as without this working properly we
    can wait forever. 
    '''    
    field = MockFieldInterface('fred',None)
    assert field.get_timeout(None) == field.def_timeout
    assert field.get_timeout(1) == 1 
    
def test_timeout_init_empty():    
    field = MockFieldInterface('fred')
    assert field.get_timeout(None) == field.def_timeout
    assert field.get_timeout(1) == 1 

def test_timeout_init_3():    
    field = MockFieldInterface('fred',3)
    assert field.get_timeout(None) == 3
    assert field.get_timeout(2) == 2 
