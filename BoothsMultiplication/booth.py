from bitstring import BitArray

def booth(m, r, x, y):
    totalLength = x + y + 1
    a = BitArray(int=m, length=totalLength) << (y+1)
    #a = ma << (y+1)
    s = BitArray(int=-m, length=totalLength) << (y+1)
    p = BitArray(int=r, length=y)
    p.prepend(BitArray(int=0, length=x))
    p = p << 1

    for i in range(1,y+1):
        if p[-2:] == '0b01':
            p = BitArray(int=p.int + a.int, length=totalLength)
        if p[-2:] == '0b10':
            p = BitArray(int=p.int + s.int, length=totalLength)
        p = arith_shift_right(p, 1)

    p = arith_shift_right(p, 1)
    return p.int

def arith_shift_right(x, amt):
    l = x.len
    x = BitArray(int=(x.int >> amt), length=l)
    return x

if __name__ == "__main__":
    print(booth(7,2,4,4))
