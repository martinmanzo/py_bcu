# -*- coding: utf-8 -*-


class BcuWsError(Exception):
    def __init__(self, code, message):
        self.message = "Código {0}: {1}".format(
            str(code),
            str(message)
        )
