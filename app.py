# Hi hello how are you

def primary_num():
    prime_n=[]
    for num in range(101):
        
        for i in range(2,int(num/2)):
            if num%2==0:
                # print("not prime")
                break
        else:
            # print("prime")
            prime_n.append(num)
    print(prime_n)
primary_num()
print()

