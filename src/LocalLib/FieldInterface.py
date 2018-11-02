#############################################################################################
#
# FieldInterface : define a common interface for "fields"
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

class FieldNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


   
class FieldInterface(object):
    error = None
    def_timeout = 5 

    def __init__(self, name,timeout=None):
        self.name = name
        self.reset_error()

        if timeout == None: 
            self.timeout = FieldInterface.def_timeout
        else:
            self.timeout = timeout

    def raise_not_found(self, message=None):
        """
        Raise a Field Not found error
        :param message: Error Message
        :return: Raises an error so no return ...
        """
        if message is None:
            self.error = "Unable to find field {}".format(self.name)
        else:
            self.error = message
        raise FieldNotFoundError(self.error)

    def reset_error(self):
        """
        Blank out the error
        :return:
        """
        self.error = None
        
    def get_timeout(self,timeout=None):
        if timeout == None:
            return self.timeout
        return timeout  

    def get_error(self):
        """
        :return: The last error messageget_value
        """
        return self.error

    def get_value(self, driver, reference=None,timeout=None):
        """
        return the value of the specified element
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: text string
        """
        return self.get_element(driver, reference,timeout).text

    def _get_element(self, driver, reference=None,timeout=None):
        """FieldNotFoundError
        low level implementation of get_element
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: Selenium Element
        """
        raise NotImplementedError()


    def get_element(self, driver, reference=None,timeout=None):
        """
        return the specified element
        :param driver: Selenium Driver
        :param reference: (optional) Identifier of the specific item (where the element is not enough)
        :return: Selenium Element
        """
        self.reset_error()
        return self._get_element( driver, reference,timeout)

    def is_valid(self, driver, reference=None,timeout=None):
        """
        Check the validity of the field.
        If getting the field value returns an error (other than NotFound) then
        the error is propagated

        :param driver: Selenium Driver
        :return: True if field is valid, False otherwise
        """
        try:
            self.get_element(driver, reference,timeout)
        except FieldNotFoundError:
            return False

        return True
