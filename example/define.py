# This Python file uses the following encoding: utf-8

from PySide6.QtCore import Property, QObject, Signal


def Singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper
