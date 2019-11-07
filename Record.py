from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox

from GUI_elements import *
from JsonMng import loads, dumps


class Record(ABC):
    @property
    def __rec(self):
        raise NotImplementedError

    @abstractmethod
    def str_value(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @classmethod
    @abstractmethod
    def add_rec(cls):
        pass

    @classmethod
    @abstractmethod
    def mod_rec(cls):
        pass

    @classmethod
    @abstractmethod
    def del_rec(cls):
        pass

    @classmethod
    @abstractmethod
    def disp_rec(cls):
        pass

    @classmethod
    @abstractmethod
    def get_rec(cls, n):
        pass

    @classmethod
    @abstractmethod
    def load_json(cls):
        pass

    @classmethod
    @abstractmethod
    def write_json(cls):
        pass
