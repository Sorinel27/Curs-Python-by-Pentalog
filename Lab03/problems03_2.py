import functools
import operator
def main():
    n = int(input())
    l = generator(n)
    print("The sum of the Fibonacci list is : ", end="")
    print(functools.reduce(operator.add, l))

def generator(n):
    n1, n2 = 0, 1
    l = []
    if n == 1:
        return n1
    for i in range(n):
        l.append(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return l


if __name__ == "__main__":
    main()