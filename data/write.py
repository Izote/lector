from time import time
from utils import *


def write(
        content: list,
        filename: str = None,
        extension: str = 'txt'
) -> None:
    """
    Takes a List and writes it as a file ('txt' by default).
    Unless provided, the filename is stored as a timestamp.

    :param content: a List or List-like object instance.
    :param filename: the output filename (minus extension), if provided.
    :param extension: desired file extension, defaults to 'txt'.
    :return: none
    """
    if filename is None:
        filename = int(time())

    filepath = join(LIB_DIR, f'{filename}.{extension}')
    with open(filepath, 'w') as file:
        for line in content:
            print(line, file=file)
