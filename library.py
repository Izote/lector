from os.path import join
from pickle import dump
from pandas import DataFrame
from utils import LIB_DIR


class Library:
    def __init__(self, sources: list) -> None:
        # General placeholder for concept; this should eventually wrap
        # around content files and prep text for Keras, TensorFlow, etc.
        source_list = []
        for source in sources:
            source_list.append({
                'source': []
            })

        self.__collection = DataFrame(source_list)

    def __str__(self) -> str:
        return self.__collection.__str__()

    @property
    def collection(self) -> DataFrame:
        return self.__collection

    def save(self, filename: str) -> None:
        with open(join(LIB_DIR, filename), 'wb') as file:
            dump(self, file)
