# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа


class CustomException(Exception):
    pass


class LevelError(CustomException):
    pass


class AccessError(CustomException):
    pass
