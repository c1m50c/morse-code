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
    
    return result


def decode(string: str) -> str:
    """
        Decodes a string containing morse code into english and digits.
        
        ## Parameters
        ```py
        string: str # String to Decode.
        ```
    """
    
    global LETTERS
    global NUMBERS
    
    # Swap the Keys and Values for looking up the codes contained in the string.
    LETTERS_S: Dict[str, str] = { value: key for key, value in LETTERS.items() }
    NUMBERS_S: Dict[str, int] = { value: key for key, value in NUMBERS.items() }
    
    split_str: List[str] = string.split(" ")
    result: str = ""
    
    for code in split_str:
        if code in LETTERS_S:
            result += LETTERS_S[code]
        elif code in NUMBERS_S:
            result += str(NUMBERS_S[code])
    
    return result