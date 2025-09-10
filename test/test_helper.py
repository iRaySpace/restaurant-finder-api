from app.helper import encode_str


def test_encode_str_returns_encoded():
    encoded_str = encode_str("test test")
    assert encoded_str == "test%20test"
