class FenanpayNotFoundException(Exception):
    def __init__(self, message, *args):
        self.msg = message
        super().__init__(message, *args)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}"
