# **morse-code**

[![Tests](https://github.com/c1m50c/morse-code/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/c1m50c/morse-code/actions/workflows/tests.yml)

Morse Code Encoder & Decoder written in Python.


## **Installing Requirements & Running**
```bash
# Install Required Packages with the `pip` package manger.
$ cd morse-code
$ pip3 install -r ./requirements.txt
```

```bash
# Run the Application with `python3`.
$ cd morse-code
$ python3 src/main.py
...
```


## **Examples**
```bash
message:$ we out here
Encoded: .-- . --- ..- - .... . .-. . 
Decoded:
```

```bash
message:$ morse code -- --- .-. ... . -.-. --- -.. .
Encoded: -- --- .-. ... . -.-. --- -.. . -....- -....- -....- -....- -....- .-.-.- -....- .-.-.- .-.-.- .-.-.- .-.-.- .-.-.- -....- .-.-.- -....- .-.-.- -....- -....- 
-....- -....- .-.-.- .-.-.- .-.-.- 
Decoded: MORSECODE
```


## **Encodable Characters**
```yml
aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ # English Alphabet
,?:-"()=@+_'/;.!&$ # Punctuation Symbols
012345679 # Digits
```