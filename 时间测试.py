# # import time
# #
# # a = list(range(20))
# # # t1 = time.time()
# # # for i in range(len(a)):
# # #     a[i] = a[i] + 1
# # # t2 = time.time()
# # # print("using for", t2 - t1)
# # print(a)
# # t3 = time.time()
# # a = [i + 1
# #      for i in a
# #      if i % 2 == 0]
# # print(a)
# # t4 = time.time()
# # print("using comprehension", t4 - t3)
#
# a=[[1,2,7],
#    [3,4],
#    [5,6,9]]
#
# for c,b in a:
#     print(c)
#
#

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f1=fib()
f2=fib()
for i in range(20):
    print("f1",f1.__next__())
    if i>10:
        print("f2",f2.__next__())
