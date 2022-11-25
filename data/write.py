from re import search
from utils import *


URL_REGX = r'(?<=/)[A-Za-z0-9]+(?=\.htm)'


def write(text_lines: list, filename: str, extension: str = 'txt') -> None:
    """
    Writes a List to the provided filename to the library directory with
    a default 'txt' file extension. If the provided filename is a URL of some
    kind, it will be truncated to allow for local storage.

    :param text_lines:
    :param filename:
    :param extension:
    :return:
    """
    if filename.find('http') >= 0:
        filename = search(URL_REGX, filename).group()

    filepath = join(LIB_DIR, filename + '.' + extension)
    with open(filepath, 'w') as file:
        for line in text_lines:
            print(line, file=file)
