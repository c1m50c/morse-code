from typing import Dict, List


# Dictionary containing english letters with their morse code counter-parts.
LETTERS: Dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..--.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


# Dictionary containing digits with their morse code counter-parts.
NUMBERS: Dict[int, str] = {
    0: "-----",
    1: ".----",
    2: "..---",
    3: "...--",
    4: "....-",
    5: ".....",
    6: "-....",
    7: "--...",
    8: "---..",
    9: "----.",
}


# Dictionary containing punctuation symbols with their morse code counter-parts.
PUNCTUATION: Dict[str, str] = {
    ",": "--..--",
    "?": "..--..",
    ":": "---...",
    "-": "-....-",
    "\"": ".-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "=": "-...-",
    "@": ".--.-.",
    "+": ".-.-.",
    "_": "..--.-",
    "'": ".----.",
    "/": "-..-.",
    ";": "-.-.-.",
    ".": ".-.-.-",
    "!": "-.-.--",
    "&": ".-...",
    "$": "...-..-",
}


# Swap the Keys and Values for looking up the codes contained in the string.
LETTERS_VK: Dict[str, str] = { value: key for key, value in LETTERS.items() }
NUMBERS_VK: Dict[str, int] = { value: key for key, value in NUMBERS.items() }
PUNCTUATION_VK: Dict[str, str] = { value: key for key, value in PUNCTUATION.items() }


def encode(string: str) -> str:
    """
        Encodes a string into morse code.
        
        ## Parameters
        ```py
        string: str # String to Encode.
        ```
    """
    
    result: str = ""
    
    for char in string:
        if char.isalpha():
            result += LETTERS[char.upper()] + " "
        elif char.isdigit():
            result += NUMBERS[int(char)] + " "
        elif char in PUNCTUATION:
            result += PUNCTUATION[char] + " "
    
    return result


def decode(string: str) -> str:
    """
        Decodes a string containing morse code into english, digits and punctuation symbols.
        
        ## Parameters
        ```py
        string: str # String to Decode.
        ```
    """
    
    split_str: List[str] = string.split(" ")
    result: str = ""
    
    for code in split_str:
        if code in LETTERS_VK:
            result += LETTERS_VK[code]
        elif code in NUMBERS_VK:
            result += str(NUMBERS_VK[code])
        elif code in PUNCTUATION_VK:
            result += PUNCTUATION_VK[code]
    
    return result