from __future__ import annotations
from typing import TYPE_CHECKING
from time import sleep
from web.get_html import get_html
from web.get_tag import get_tag

if TYPE_CHECKING:
    from bs4 import BeautifulSoup


def read_url(
        url: str | list,
        tag: str,
        attribute: str,
        find_all: bool = True,
        skip: int = None,
        wait: int = None,
        parser: str = 'html.parser'
) -> list:
    def read_tag(doc: BeautifulSoup) -> str:
        return get_tag(
            doc,
            tag=tag,
            attribute=attribute,
            find_all=find_all,
            skip=skip
        )

    html_doc = []
    if isinstance(url, str):
        html_doc.append(get_html(url, parser=parser))
    elif isinstance(url, list):
        for u in url:
            html_doc.append(get_html(u, parser=parser))

            if wait:
                sleep(wait)
    else:
        raise NotImplementedError

    return [read_tag(doc) for doc in html_doc]
