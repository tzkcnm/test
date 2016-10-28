# -*- coding:utf-8 -*-

def main():
    L = range(1, 11)

    def sample():
        for x in L:
            if x > 7:
                return
            if x % 4 == 0:
                yield x

    # for x in sample():
        #     print x

    # items = sample()
    # print items
    # print next(items)
    # print next(items)
    # print next(items)


   pred1 = lambda x: x % 2 == 0
   pred2 = lambda x: x < 8
   cond = lambda x: pred1(x) and pred2(x)

   # for x in filter(cond, L):
   #     print x

   '''
   ジェネレータの利点
   1. 手続き的に書ける
   2. 遅延できる
   '''

   def cond(xs):
       for x in xs:
           if x >= 8:
               return
           if x % 2 != 0:
               continue
           yield x

    for x in cond(L):
        print x


if __name__ == '__main__':
    main()

