from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bs4 import BeautifulSoup


def get_tag(
        html_doc: BeautifulSoup,
        tag: str,
        attribute: str,
        find_all: bool = True,
        skip: int = None
) -> list:
    """
    Extracts a chosen output from the provided HTML tag.

    :param html_doc: an HTML documents as a BeautifulSoup object instance.
    :param tag: the desired HTML tag.
    :param attribute: the desired attribute to extract (e.g., 'text', 'href').
    :param find_all: read all tags (True) or just the first (False).
    :param skip: if provided, the output will skip this number of elements.
    :return: raw text as a List.
    """
    html_tag = html_doc.find_all(tag) if find_all else html_doc.find(tag)

    if attribute == 'text':
        result = [tag.text for tag in html_tag]
    else:
        result = [tag.get(attribute) for tag in html_tag]

    if skip:
        return result[skip:]
    else:
        return result
