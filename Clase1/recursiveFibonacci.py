def fibo(t1, t2, count):
    if count < 100:
        print(t1)
        fibo(t2, t1+t2, count + 1)

if __name__ == "__main__":
    fibo(0, 1, 0)
    
