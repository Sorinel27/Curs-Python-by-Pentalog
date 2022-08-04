#Fratean Sorin problema lab 1
import csv
import datetime


def main():
    file = open('problem1.csv', 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(len(rows))
    count = 0
    for x in rows:
        if 'B' in x[3].split("|"):
            count += 1
    print(count)
    moto = []
    for x in rows:
        if 'A' in x[3].split("|") and varstamin(x[2]):
            moto.append(x)
    moto.sort()
    print(moto)
    file.close()


def varstamin(datan):
    date = datetime.datetime.strptime(datan, '%d/%m/%Y')
    now = datetime.datetime.today()
    if now - date > datetime.timedelta(days=365 * 21):
        return True


if __name__ == '__main__':
    main()