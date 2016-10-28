# -*- coding:utf-8 -*-


# class SkipMe(Exception):
#     pass


SkipMe = type('SkipMe', (Exception,), {})


class ContextManager(object):
    def __enter__(self):
        print '=== START ==='

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is SkipMe:
            return True
    print '=== END ==='


def main():
                                                    
    # fp = open('/tmp/_', 'r')

    # try:
    #     for line in fp:
    #         print line
    # finally:
    #     fp.close()

    # with open('/tmp/_', 'r') as fp:
    #     for x in fp:
    #         print x

    text = '012?3'
    for i, x in enumerate(text):
        with ContextManager():
            if i == 3:
                raise SkipMe()
            print int(x)


if __name__ == '__main__':
    main()
