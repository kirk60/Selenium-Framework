#############################################################################################
#
# SFField : Used to find field in a selenium based browser
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
from selenium.common.exceptions import NoSuchElementException
from LocalLib.SeleniumShortcuts import SeleniumShortcuts


class SFField(FieldInterface):

    def __init__(self, name, selector_type, selector_value, required='False', ref=None):
        """

        :param name: name of the field
        :param selector_value: The string that the selector will match
        :param selector_type: EG css, name ...
        :param required: Is this a required field
        :param ref: some sort of reference as to why the field is here
        """

        self.selector_type = SeleniumShortcuts.get_selector(selector_type)

        super().__init__(name)
        self.selector_value = selector_value
        self.required = required
        self.ref = ref

    def to_string(self):
        return "{},{},{},{},{},".format(self.name, self.selector_type, self.selector_value, self.required, self.ref)

    def get_element(self, driver):
        """
        Using the specified selector type & value locate the element
        :param driver: the selenium webDriver
        :return: the Element (if found)
        """

        try:
            return driver.find_element(self.selector_type, self.selector_value)
        except NoSuchElementException as e:
            self.raise_not_found()

    def get_value(self, driver):
        return self.get_element(driver).text
