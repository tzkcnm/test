# -*- coding:utf-8 -*-


def foo(func):
    def _foo(*args, **kwargs):
        print 'start...'
        try:
            return func(*args, **kwargs)
        finally:
            print '...end'
    return _foo


@foo
def bar(x, y):
    return x + y

@foo
def baz(x, y):
    return x * y


def main():
    print bar(100, 20), baz(10, 67)


if __name__ == '__main__':
    main()
