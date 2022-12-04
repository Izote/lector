from __future__ import annotations
from os.path import join
from pickle import load
from typing import TYPE_CHECKING
from utils import LIB_DIR

if TYPE_CHECKING:
    from library import Library


def get_library(filename: str) -> Library:
    with open(join(LIB_DIR, filename), 'rb') as file:
        lib = load(file)

    return lib
