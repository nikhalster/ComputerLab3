import random


def brutePrime(n):
    isPrime = True
    i = 2
    while(i < n/2):
        if n % i == 0:
            isPrime = False
            return isPrime
        i += 1
    return isPrime

def millerRabin(n):
    iter = 100
    i = 0
    isPrime = True
    while(i < iter):
        randomCheck = random.randint(2, (n-2))
        if n % randomCheck == 0:
            isPrime = False
            return isPrime
        i += 1
    return isPrime

if __name__ == "__main__":
    p = long(raw_input("Enter P"))
    q = long(raw_input("Enter Q"))
    g = long(raw_input("Enter G"))
    print("Brute force {}".format(brutePrime(q)))
    print("Miller Rabin {}".format(millerRabin(q)))

    if len(bin(q)) == 160:
        print("Q = 160")
    else:
        print("Q != 160")

    if ((p - 1) % q) == 0:
        print("Q divides (p-1)")
    else:
        print("Q doesnt divide (p-1)")

    if len(bin(p)) >= 512 and len(bin(p)) <= 1024:
        print("Number of bits of p is between 512 and 1024")
    else:
        print("Number of bits of p is not between 512 and 1024")

    if (pow(2, ((p - 1) / q)) % p) == g:
        print("G in right form")
    else:
        print("G not in right form")

