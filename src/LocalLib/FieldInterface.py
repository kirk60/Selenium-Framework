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

    def __init__(self, name):
        self.name = name
        self.reset_error()

    def raise_not_found(self, message=None):
        """
        Raise a Field Not found error
        :param message: Error Message
        :return: Raises an error so no return ...
        """
        self.error = message
        if message is None:
            self.error = "Unable to find field {}".format(self.name)
        raise FieldNotFoundError(self.error)

    def reset_error(self):
        """
        Blank out the error
        :return:
        """
        self.error = None

    def get_error(self):
        """

        :return: The last error message
        """
        return self.error

    def get_value(self):
        """
        Implementation dependent. Get record value.
        :return:
        """
        self.reset_error()
        raise NotImplementedError()

    def is_valid(self):
        """
        Check the validity of the field.
        If getting the field value returns an error (other than NotFound) then
        the error is propagated

        :return: True if field is valid, False otherwise
        """
        try:
            self.get_value()
        except FieldNotFoundError:
            return False

        return True