from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bs4 import BeautifulSoup


def get_tag(
        html_doc: BeautifulSoup,
        tag: str,
        find_all: bool = True
) -> list:
    """
    Extracts text from the provided HTML tag. By default, this will extract
    text from *all* such tags.

    :param html_doc: an HTML document as a BeautifulSoup object instance.
    :param tag: the desired HTML tag.
    :param find_all: read all tags (True) or just the first (False).
    :return: raw text as a List.
    """
    html_tag = html_doc.find_all(tag) if find_all else html_doc.find(tag)

    return [tag.text for tag in html_tag]
