class BcuWsError(Exception):
    """
    Represents an error raised in the context of BCU Web Services.

    This class defines a custom exception to handle errors that occur during
    interactions with BCU Web Services. It provides a formatted error message
    that includes an error code and a descriptive message.

    :ivar message: Formatted error message containing the error code and
        description.
    :type message: str
    """
    def __init__(self, code, message):
        self.message = "Código {0}: {1}".format(
            str(code),
            str(message)
        )
