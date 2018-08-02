#
# LocalLib/SFArrayField
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

"""Selector that returns Multiple elements

Some Web selectors return multiple elements, this is the simplest case
1 ) All elements are returned by a single call to get_elements
2 ) They are referenced by an index



# Todo:

"""


from LocalLib.SFField import SFField
from selenium.common.exceptions import NoSuchElementException


class SFArrayField(SFField):

    def __init__(self, name, selector_type=None, selector_value=None, required='False', ref=None):
        """

        :param name: name of the field
        :param selector_value: The string that the selector will match
        :param selector_type: EG css, name ...
        :param required: Is this a required field
        :param ref: some sort of reference as to why the field is here
        """
        super().__init__(name, selector_type, selector_value, required, ref)

    def to_string(self,name ="SFArrayField"):
        return super.to_string(name)

    def get_element(self, driver, reference=None):
        """
        return the specified element
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: Selenium Element
        """

        try:
            values = driver.find_elements(self.selector_type, self.selector_value)
            if reference is None:
                return values
            return values[reference]
        except NoSuchElementException as e:
            self.raise_not_found()

    def get_value(self, driver, reference=None):
        """
        return the specified elements text value
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: Selenium Element
        """
        return self.get_element(driver, reference).text
