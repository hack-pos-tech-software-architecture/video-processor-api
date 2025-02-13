class UserAlreadyExistsException(Exception):
    def __init__(self, message="User already exists."):
        super().__init__(message)
        self.message = message


class UserNotFoundException(Exception):
    def __init__(self, message="User not found."):
        super().__init__(message)
        self.message = message


class EntityNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class EntityAlreadyExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class NotAuthorizedException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
