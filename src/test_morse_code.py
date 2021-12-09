from morse_code import encode, decode


def test_hello_world_encoding():
    assert encode("Hello, World!") == ".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.-- "


def test_hello_world_decoding():
    assert decode(".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.--") == "HELLO,WORLD!"


if __name__ == "__main__":
    test_hello_world_encoding()
    test_hello_world_decoding()