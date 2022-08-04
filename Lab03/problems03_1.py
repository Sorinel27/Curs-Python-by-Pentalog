def main():
    n = int(input("How many strings?:\n"))
    a = ""
    for i in range(n):
        letters = input()
        if letters == "\n" or letters == "\t":
            letters = ""
        a = a + concatenate(letters)
    print(a)


def concatenate(b):
    for i in range(len(b)):
        if i == 0:
            b = b.capitalize()
    return b


if __name__ == '__main__':
    main()
