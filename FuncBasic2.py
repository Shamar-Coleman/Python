#! First

#! First


def countDown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result


print(countDown(10))


#! Second


def printAndReturn(x):
    print(x[0])
    return x[1]


x = printAndReturn([1, 2])
print(x)


#! Third


def plusLength(arr):
    return arr[0] + len(arr)


total = plusLength([10, 20, 20, 4, 5, 6])
print(total)


#! Four


def valueGreaterThanSecond(x):
    newList = []
    count = 0
    for i in range(0, len(x), 1):
        if (x[i] > x[1]):
            newList.append(x[i])
            count = count + 1
    print(count)
    if (len(newList) < 2):
        return False
    return newList


print(valueGreaterThanSecond([5, 2, 3, 2, 1, 4]))


#! Five


def lengthAndValue(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList


print(lengthAndValue(5, 2))