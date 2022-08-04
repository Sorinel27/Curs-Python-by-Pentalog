# Fratean Sorin Problema lab 2
def main():
    l = [9, [4, 5, 1], 5, [[5, 3], 1]]
    r = []
    ok = 1.79
    count = 0
    listNormalizer(l, r)
    r.sort()
    print(r)
    for i in range(len(r)):
        if r[i] != ok:
            for j in range(len(r)):
                if r[i] == r[j]:
                    count += 1
            print(r[i], ":", count)
            count = 0
            ok = r[i]


def listNormalizer(list, result):
    for i in range(len(list)):
        if len(str(list[i])) > 1:
            ok(list[i], result)
        else:
            result.append(list[i])


def ok(list, result):
    for i in range(len(list)):
        if len(str(list[i])) > 1:
            ok(list[i], result)
        else:
            result.append(list[i])


if __name__ == '__main__':
    main()
