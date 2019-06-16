def isPrime(x):
    if x<= 1:
        return False
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
def Primes(start,end):
    for i in range(start,end):
        if isPrime(i):
            yield i
def sumPrimes(Primes):
    sum = 0
    for i in Primes:
        sum+=i
    return sum
def main():
    a=int(input('scanf the start:'))
    b=int(input('scanf the end:'))
    print([x for x in Primes(a,b)])
    print(sumPrimes(Primes(a,b)))
if __name__ == "__main__":
    main()

