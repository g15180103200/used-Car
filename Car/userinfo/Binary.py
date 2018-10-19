# Binary.py
# def BinarySearch(l, x):
#     l.sort()
#     low = 0
#     high = len(l) - 1
#     while low < high:
#         mid = (low + high) // 2
#         if l[mid] < x:
#             low = mid + 1
#         elif l[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1


def BinarySearch(array, t):
    array.sort()
    low = 0
    height = len(array) - 1
    while low <= height:
        mid = (low + height) // 2
        if array[mid] < t:
            low = mid + 1

        elif array[mid] > t:
            height = mid - 1

        else:
            return mid

    return -1


if __name__ == "__main__":
    print(BinarySearch([1, 2, 3, 34, 56, 57, 78, 87], 78))