from math import sqrt

def isPrime(n):
    if(n==0):
        return False
    isPrime = True
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            isPrime = 0
            break
    return isPrime


def solve(inputList):
    primeList = []
    for number in inputList:
        if (isPrime(number)):
            primeList.append(number)
    primeList.sort()
    return primeList

#Test case 1
primeList1=[1,2,3,4,5]
print(solve(primeList1)) #Output [1,2,3,5]
#Test case 2
primeList2=[0,1,3,5]
print(solve(primeList2)) #Output [1,3,5]
#Test case 3
primeList3=[5,4,3,2,1,0]
print(solve(primeList3)) #Output [1,2,3,5]

