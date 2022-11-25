from requests import get
from bs4 import BeautifulSoup


def get_html(
        url: str,
        parser: str = 'html.parser'
) -> BeautifulSoup:
    """
    Obtains the HTML text from the web address provided.

    :param url: desired web address.
    :param parser: parser used to extract HTML text; defaults to 'html.parser'.
    :return: an HTML document as a BeautifulSoup object instance.
    """
    request = get(url)

    return BeautifulSoup(request.text, parser)
