import urllib.parse


def encode_str(data: str):
    return urllib.parse.quote(data)