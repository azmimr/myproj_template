import logging

module_logger = logging.getLogger('mypackage.module_one')


class MyClass:
    """This is a template class. There are parameters in the initialization
    """

    def __init__(self):
        self.logger = logging.getLogger('mypackage.module_one.MyClass')
        self.logger.info("Creating an instance of MyClass")

        self.message = "This is in the Class"

        return

    def my_function(self, text=""):
        """Displays a message from user or a default.

        :param text: Text to display, defaults to ""
        :type text: str, optional

        Example:
        >>>MyClass.myfunction("Test message")
        Test message
        """

        self.logger.info("Displays a message")
        if text:
            print(text)
        else:
            print(self.message)
        return
