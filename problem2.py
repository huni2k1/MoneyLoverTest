def fibonacci_nth(n):
    if(n<=0):
        raise ValueError("Input must be positive integer")
    tmp1,tmp2=0,1
    if(n==1):
        return tmp1
    if(n==2):
        return tmp2
    for i in range(3,n+1):
        tmp = tmp1+tmp2
        tmp1=tmp2
        tmp2=tmp
    return tmp2

#Test case 1:
try:
    print(fibonacci_nth(-1))
except ValueError as err:
    print(err)    #Output error message
#Test case 2:
print(fibonacci_nth(5)) #Output 3 
#Test case 3:
print(fibonacci_nth(11)) #Output 55