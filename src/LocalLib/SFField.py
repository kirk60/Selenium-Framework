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

    def __init__(self, name, selector_type=None, selector_value=None, required='False', ref=None):
        """

        :param name: name of the field
        :param selector_value: The string that the selector will match
        :param selector_type: EG css, name ...
        :param required: Is this a required field
        :param ref: some sort of reference as to why the field is here
        """

        #
        #   barf .. Fake function overloading
        #
        #
        if selector_type is None:
            fields = name + ",,,,,"
            fields = fields.split(',')
            name = fields[0]
            selector_type = fields[1]
            selector_value = fields[2]
            if len(fields[3]) == 0:
                required = False
            else:
                required = fields[3]
            if len(fields[3]) == 0:
                ref = None
            else:
                ref = fields[4]


        super().__init__(name)
        self.selector_type = SeleniumShortcuts.get_selector(selector_type)
        self.selector_value = selector_value
        self.required = required
        self.ref = ref

    def to_string(self,name =None):
        if name is None:
            name = "SFField"
        return "{} : {},{},{},{},{},".format(name,self.name, self.selector_type, self.selector_value, self.required, self.ref)

    def _get_element(self, driver, reference=None):
        """
        return the specified element
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: Selenium Element
        """

        try:
            return driver.find_element(self.selector_type, self.selector_value)
        except NoSuchElementException as e:
            self.raise_not_found()

