from morse_code import encode, decode


def test_hello_world_encoding():
    assert encode("Hello, World!") == ".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.--"


def test_hello_world_decoding():
    assert decode(".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.--") == "HELLO,WORLD!"