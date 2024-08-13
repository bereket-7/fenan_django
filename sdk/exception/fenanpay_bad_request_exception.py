class FenanpayBadRequestException(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}"
