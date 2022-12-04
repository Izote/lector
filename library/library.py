from re import search
from os.path import join
from pickle import dump
from pandas import DataFrame
from data.clean_text import clean_text
from web.get_html import get_html
from web.get_tag import get_tag
from utils import LIB_DIR


class Library:
    def __init__(self) -> None:
        self.__source = []
        self.__filenames = []
        self.__collection = DataFrame()

    @property
    def collection(self) -> DataFrame:
        return self.__collection

    @property
    def source(self) -> list:
        return self.__source

    def save(self, filename: str) -> None:
        with open(join(LIB_DIR, filename), 'wb') as file:
            dump(self, file)
