from morse_code import encode, decode


def main():
    while True:
        inp: str = input(">>> ")
        
        if inp.isspace():
            return
        else:
            print(encode(string=inp))
            print(decode(string=inp))


if __name__ == "__main__":
    main()