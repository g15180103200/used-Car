# # mysort.py
# s1 = "program"
# s2 = "grap"
# s3 = ""
# s4 = ""
# for a in s1:
#     if a not in s2:
#         s4 += a
# for x in s2:
#     for y in s1:
#         if y == x:
#             s3 += y
# print(s3+s4)


# l = [73,74,75,71,70,76,72,73]
# L = []
# length = len(l)
# for index,value in enumerate(l):
#     k = index
#     while k < length:
#         if l[k] > value:
#             print(l[k])
#             L.append(k-index)
#             break
#         k += 1
#     if k >= length:
#         L.append("None")

# print(L)
# import itertools


# def mysum(l, k):
#     i = 1
#     length = len(l)
#     while i <= length:
#         L = list(itertools.permutations(l, i))
#         for x in L:
#             if sum(x) == k:
#                 print(x)
#         i += 1
# def fun(n, k):
#     if k == 1:
#         return [[i + 1] for i in range(n)]
#     result = []
#     if n > k:
#         result = [r + [n] for r in fun(n - 1, k - 1)] + fun(n - 1, k)
#     else:
#         result = [r + [n] for r in fun(n - 1, k - 1)]
#     return result
# print(fun(4,3))
def printMatrixZigZag(m):
    def printLevel(m, tR1, tC1, tR2, tC2, flag):
        if flag:
            while tR2 != tR1 - 1:
                print(m[tR2][tC2], end=' ')
                tR2 -= 1
                tC2 += 1
        else:
            while tR1 != tR2 + 1:
                print(m[tR1][tC1], end=' ')
                tR1 += 1
                tC1 -= 1

    tR1 = tC1 = tR2 = tC2 = 0
    dR = len(m) - 1
    dC = len(m[0]) - 1
    flag = True
    while tR1 <= dR and tC2 <= dC:
        printLevel(m, tR1, tC1, tR2, tC2, flag)
        tR1 = tR1 if tC1 != dC else tR1 + 1
        tC1 = tC1 + 1 if tC1 != dC else tC1
        tC2 = tC2 if tR2 != dR else tC2 + 1
        tR2 = tR2 + 1 if tR2 != dR else tR2
        flag = not flag
printMatrixZigZag([1,2,3,4,5,6,7,8,9,10])