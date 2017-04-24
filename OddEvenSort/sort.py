from threading import Thread

def swap(x, l):
    for i in range(l, len(x) -1, 2):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
            sorted = False
        if x[i] == x[i+1]:
            i = i + 2

def sort(x):
    sorted = False
    while not sorted:
        sorted = True
        t1 = Thread(target = swap(x, 0))
        t2 = Thread(target = swap(x, 1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    for i in range(0, len(x) - 1):
        if x[i] <= x[i+1]:
            sorted = False
        else:
            x = sort(x)
    return x

if __name__ == "__main__":
    a = [3,5,1,4]
    print(sort(a))