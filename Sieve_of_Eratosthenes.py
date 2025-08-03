# Enumerate primes to N in O(log logn)

n=int(input("ENter n:"))
primes=[True]*(n+1) #COnsider all elements as prime
primes[0]=primes[1]=False
i=2
while i*i<=n:
  if primes[i]:
    for j in range(i*i,n+1,i):
      primes[j]=False
  i+=1
#print(primes)
prime_nos=[]
for i in range(2,n+1):
  if primes[i]:
    prime_nos.append(i)
print(prime_nos