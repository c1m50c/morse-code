from typing import Dict, List


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
    result: str = ""
    
    for char in string:
        if char.isalpha():
            result += LETTERS[char.upper()] + " "
        elif char.isdigit():
            result += NUMBERS[int(char)] + " "
    
    return result


def decode(string: str) -> str:
    global LETTERS
    global NUMBERS
    
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