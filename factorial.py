

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
      # i+=1

    return fact




res=fact(5)
print(res)
