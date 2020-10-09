def lothar(n1):
    count = 0
    while n1 != 1:
        if n1 % 2 == 0:
            n1 /= 2
        else:
            n1 *= 3
            n1 += 1
        count += 1
    return count
if __name__ == "__main__":
    print(lothar(int(input())))
