import json
from past.builtins import raw_input


class Serializer:
    def as_string(self):
        raise NotImplementedError

    def __str__(self):
        str(self.as_string())

    def __len__(self):
        len(self.as_string())

    def __add__(self, other):
        ok = str(self) + '\n' + str(other)
        if len(ok) > 512:
            raise self.TooLongException
        return ok


class ListSerializer(Serializer):
    def __init__(self, list=[]):
        super().__init__(list)
        self.list = list

    def as_string(self):
        return json.dumps(self.list)


class DictSerializer(Serializer):
    def __init__(self, dic=[]):
        super().__init__(dic)
        self.dic = dic

    def as_string(self):
        return json.dumps(self.dic)


if __name__ == "__main__":
    l = []
    n = int(input("Enter a the number of elements in your list: "))
    for i in range(n):
        ok = int(input("Enter the element: "))
        l.append(ok)
    lista = Serializer(list=l)
    m = int(input("Enter a the number of datas for dictionary: "))
    print("Enter the elements of the dictionary")
    d = dict(raw_input().split() for i in range(m))
    dictionar = Serializer(dic=d)
    print(lista.list)
    print(dictionar.dic)
