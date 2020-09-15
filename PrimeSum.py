#PrimeSum.py
def isPrime(a):
    if a<=1:
        return False
    if a==2:
        return True
    else:
        for i in range(2,a):
            if a%i==0:
                return False
    return True
        
sum = 0

for i in range(101):
    if isPrime(i):
        sum+=i
print(sum)
