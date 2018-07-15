class FieldNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


#
#   Generic Field interface
#
#

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
