from re import sub, UNICODE


def clean_text(
        raw_text: str | list,
        pattern: str
) -> str | list:
    """
    Accepts raw text as a String or List (of Strings), returning output of
    the same type with pattern-characters removed. The default pattern controls
    for special, non-punctuation characters. Empty-string elements ('')
    are removed from List outputs.

    :param raw_text: raw text as a String or List (of Strings).
    :param pattern: a regular expression pattern to be removed from `raw_text`.
    :return: cleaned text as a String or List (of Strings).
    """
    def remove_chars(text: str) -> str:
        return sub(pattern, '', text, UNICODE).strip()

    if isinstance(raw_text, list):
        return [t for t in [remove_chars(rt) for rt in raw_text] if t != '']
    elif isinstance(raw_text, str):
        return remove_chars(raw_text)
    else:
        raise TypeError('`clean_text` accepts only `list` or `str` type')
