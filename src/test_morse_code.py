from morse_code import encode, decode


def test_hello_world_encoding():
    assert encode("Hello, World!") == ".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.-- "


def test_hello_world_decoding():
    assert decode(".... . .-.. .-.. --- --..-- .-- --- .-. .-.. -.. -.-.--") == "HELLO,WORLD!"


def test_morse_code_endcoding():
    assert encode("morse-code") == "-- --- .-. ... . -....- -.-. --- -.. . "


def test_morse_code_decoding():
    assert decode("-- --- .-. ... . -....- -.-. --- -.. .") == "MORSE-CODE"


def test_digits_encoding():
    assert encode("0123456789") == "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. "


def test_digits_decoding():
    assert decode("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.") == "0123456789"


if __name__ == "__main__":
    test_hello_world_encoding()
    test_hello_world_decoding()
    test_morse_code_endcoding()
    test_morse_code_decoding()
    test_digits_encoding()
    test_digits_decoding()