# -*- coding:utf-8 -*-


def main():

    def times(items, length):
        acc = []

        for x in items:
            if len(acc) >= length:
                yield acc
                acc = []
            acc.append(x)

        if acc:
            yield acc

    data = range(1, 256)
    items = times(data, 30)

    for x in items:
        print x

if __name__ == '__main__':
    main()

